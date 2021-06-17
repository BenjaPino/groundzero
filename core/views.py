from .forms import ArtistaForm
from django.shortcuts import redirect, render
from .models import Artista


# Create your views here.
def inicio(request):  
    
    artistas = Artista.objects.all()
    datos = {
        'artistas': artistas
    }
    return render(request,'core/inicio.html',datos)


def formularioArtista(request):
    datos={'form': ArtistaForm()}
    if request.method=="POST":
        formulario=ArtistaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Artista guardado correctamente"
    return render(request,'core/formularioArtista.html', datos)

def form_mod(request,id):
    artista=Artista.objects.get(nombre=id)
    datos={'form':ArtistaForm(instance=artista)}
    if request.method=='POST':
        formulario = ArtistaForm(data=request.POST,instance=artista)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request,'core/form_mod.html',datos)

def form_del(request,id):
    artista = Artista.objects.get(nombre=id)
    artista.delete()
    return redirect(to=inicio)


