from django.db.models import fields
from rest_framework import serializers
from core.models import Artista, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','email','password']
class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['nombre','descripcion']
