from django.shortcuts import render, get_object_or_404, redirect
from .forms import CitaForm
from .models import Cita


# Create your views here.

def lista_citas(request):
    citas = Cita.objects.all().order_by('fecha')
    return render(request, 'lista_citas.html', {'citas':citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CitaForm()
    return render(request, 'form_cita.html', {'form':form})

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'form_cita.html', {'form':form})


def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect(f'lista')
    return render(request, 'confirmar_eliminacion.html', {'cita':cita})

