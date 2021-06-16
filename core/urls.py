from django.urls import path
from .views import inicio,formularioArtista

urlpatterns = [
    path('',inicio,name="inicio"),
    path('formularioArtista',formularioArtista,name="formulario"),
    
]