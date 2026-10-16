from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from .forms import CitaForm
from .models import Cita, Doctor


class CitasTests(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(nombre="Doctor de prueba", especialidad="General")
        self.data = {"paciente": "Paciente ficticio", "doctor": self.doctor.pk,
                     "fecha": (date.today() + timedelta(days=1)).isoformat(), "estado": "Programada"}

    def test_fechas_hoy_y_pasadas_se_rechazan(self):
        for days in (0, -1):
            with self.subTest(days=days):
                data = dict(self.data, fecha=(date.today() + timedelta(days=days)).isoformat())
                form = CitaForm(data=data)
                self.assertFalse(form.is_valid())
                self.assertIn("fecha", form.errors)

    def test_crear_editar_y_eliminar(self):
        self.assertRedirects(self.client.post(reverse("crear"), self.data), reverse("lista"))
        cita = Cita.objects.get()
        response = self.client.get(reverse("lista"))
        self.assertContains(response, "Paciente ficticio")
        self.assertContains(response, reverse("editar", args=[cita.pk]))
        self.assertContains(response, reverse("eliminar", args=[cita.pk]))
        self.assertEqual(self.client.get(reverse("editar", args=[cita.pk])).status_code, 200)
        self.assertRedirects(self.client.post(reverse("editar", args=[cita.pk]), dict(self.data, estado="Atendida")), reverse("lista"))
        cita.refresh_from_db()
        self.assertEqual(cita.estado, "Atendida")
        self.assertEqual(self.client.get(reverse("eliminar", args=[cita.pk])).status_code, 200)
        self.assertTrue(Cita.objects.filter(pk=cita.pk).exists())
        self.assertRedirects(self.client.post(reverse("eliminar", args=[cita.pk])), reverse("lista"))
        self.assertFalse(Cita.objects.exists())

    def test_estado_invalido_no_crea_cita(self):
        response = self.client.post(reverse("crear"), dict(self.data, estado="Inexistente"))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cita.objects.exists())

    def test_citas_inexistentes_devuelven_404(self):
        for name in ("editar", "eliminar"):
            self.assertEqual(self.client.get(reverse(name, args=[999])).status_code, 404)

    def test_listado_vacio(self):
        self.assertContains(self.client.get(reverse("lista")), "Todavía no hay citas registradas.")
