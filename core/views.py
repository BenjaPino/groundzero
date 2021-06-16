from django.shortcuts import redirect, render
from .models import Artista

# Create your views here.
def inicio(request):
    return render(request,'core\inicio.html')

def formulario(request):
    artistas= Artista.objects.all()
    datos = {
        'artistas': artistas
    }
    return render(request,'core\formulario.html', datos)

def form_Artista(request):
    return render(request,'core/form')
