from datetime import date
from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields ='__all__'

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha <= date.today():
            raise forms.ValidationError("La fecha de la cita debe ser posterior a hoy.")
        return fecha