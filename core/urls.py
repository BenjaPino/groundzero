from django.urls import path
from .views import inicio,formularioArtista,form_mod,form_del,home,artista1,artista2,artista3,registrar,iniciarsesion


urlpatterns = [
    path('',home,name="home"),
    path('formularioArtista',formularioArtista,name="formulario"),
    path('form-mod/<id>',form_mod,name="form_mod"),
    path('form-del/<id>',form_del,name="form_del"),
    path('inicio',inicio,name="inicio"),
    path('artista1',artista1,name="artista1"),
    path('artista2',artista2,name="artista2"),
    path('artista3',artista3,name="artista3"),
    path('iniciarsesion',iniciarsesion,name="iniciarsesion"),
    path('registrar',registrar,name="registrar"),
    
    
]