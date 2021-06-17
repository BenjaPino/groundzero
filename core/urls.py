from django.urls import path
from .views import inicio,formularioArtista,form_mod,form_del


urlpatterns = [
    path('',inicio,name="inicio"),
    path('formularioArtista',formularioArtista,name="formulario"),
    path('form-mod/<id>',form_mod,name="form_mod"),
    path('form-del/<id>',form_del,name="form_del"),
    
    
]