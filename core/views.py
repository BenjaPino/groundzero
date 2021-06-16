from django.shortcuts import redirect, render
from .models import Artista

# Create your views here.
def inicio(request):
    return render(request,'core\inicio.html')


def formulario(request):
    return render(request,'core/formulario.html')
