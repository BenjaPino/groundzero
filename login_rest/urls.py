from django.urls import path
from login_rest.views import  detalle_artista, lista_artista, lista_usuario

urlpatterns=[
    path('lista_usuario', lista_usuario,name="lista_usuario"),
    path('lista_artista', lista_artista,name="lista_artista"),
    path('detalle_artista/<id>', detalle_artista,name="detalle_artista"),


    
]
