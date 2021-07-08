from django.core.checks import messages
from .forms import ArtistaForm, CustomUserCreation, UsuarioForm, UserCreationForm
from django.shortcuts import redirect, render
from .models import Artista
from django.contrib.auth import authenticate, login


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


def home(request):
    return render(request, "core/home.html")

def artista1(request):
    return render(request, "core/artista1.html")

def artista2(request):
    return render(request, "core/artista2.html")

def artista3(request):
    return render(request, "core/artista3.html")

def iniciarsesion(request):
    datos={'form': UsuarioForm()}
    if request.method=="POST":
        formulario=UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Artista guardado correctamente"
            return redirect(to="home")
    return render(request,'core/formularioArtista.html', datos)

def registrar(request):
    data={
        'form':CustomUserCreation()
    }
    if request.method=='POST':
        formulario = CustomUserCreation(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.Info(request,"Registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'core/registrar.html',data)

