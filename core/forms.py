from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Artista

class ArtistaForm(ModelForm):
    class Meta:
        model = Artista
        fields=['nombre','descripcion','img_artista']