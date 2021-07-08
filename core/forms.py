from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from rest_framework.utils.field_mapping import ClassLookupDict
from .models import Artista, Usuario

class ArtistaForm(ModelForm):
    class Meta:
        model = Artista
        fields=['nombre','descripcion','img_artista']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields=['nombre','email','password']
        widgets = {
            'password' : forms.PasswordInput()
        }