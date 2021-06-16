from django.urls import path
from .views import inicio,formulario

urlpatterns = [
    path('',inicio,name="inicio"),
    path('formulario',formulario,name="formulario"),
    
]