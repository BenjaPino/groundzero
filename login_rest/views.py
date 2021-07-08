from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from core.models import Artista, Usuario
from .serializers import ArtistaSerializer, UsuarioSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_usuario(request):
    if(request.method=='GET'):
        usuario=Usuario.objects.all()
        serializer=UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    elif (request.method=='POST'):
        data=JSONParser().parse(request)
        serializer=UsuarioSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_artista(request):
    if(request.method=='GET'):
        usuario=Artista.objects.all()
        serializer=ArtistaSerializer(usuario, many=True)
        return Response(serializer.data)
    elif (request.method=='POST'):
        data=JSONParser().parse(request)
        serializer=ArtistaSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def detalle_artista(request,id):
    try:
        artista= Artista.objects.get(nombre=id)
    except Artista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        serializer=ArtistaSerializer(artista)
        return Response(serializer.data)
    if(request.method=='PUT'):
        data=JSONParser().parse(request)
        serializer=ArtistaSerializer(artista,data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        artista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)