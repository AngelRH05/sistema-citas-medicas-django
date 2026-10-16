from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    ESTADOS = (
    ('Programada', 'Programada'),
    ('Atendida', 'Atendida'),
    ('Cancelada', 'Cancelada'),
    )

    paciente = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=100, choices=ESTADOS)

    def __str__(self):
        return  f" {self.paciente} - {self.fecha}"
