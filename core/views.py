from core.forms import ArtistaForm
from django.shortcuts import redirect, render
from .models import Artista


# Create your views here.
def inicio(request):  
    return render(request,'core/inicio.html')


def formularioArtista(request):
    datos={
        'form': ArtistaForm
        }
    if request.method=='POST':
        formulario = ArtistaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos guardados correctamente"
    return render(request,'core/formularioArtista.html', datos)
