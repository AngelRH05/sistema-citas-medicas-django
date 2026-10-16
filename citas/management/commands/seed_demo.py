from datetime import date, timedelta
from django.core.management.base import BaseCommand
from citas.models import Doctor, Cita


class Command(BaseCommand):
    help = "Crea datos ficticios para explorar la aplicación localmente."

    def handle(self, *args, **options):
        doctor, _ = Doctor.objects.get_or_create(nombre="Doctor de ejemplo", especialidad="Medicina general")
        Cita.objects.get_or_create(paciente="Paciente de ejemplo", doctor=doctor,
                                  fecha=date.today() + timedelta(days=7), defaults={"estado": "Programada"})
        self.stdout.write(self.style.SUCCESS("Datos de demostración disponibles."))
