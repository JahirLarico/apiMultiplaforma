from django.shortcuts import render
from .models import Recetas
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class IndexView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, world!'})


class RecetasList(APIView):
    def get(self, request):
        recetas = Recetas.objects.all()
        serializer = RecetasSerializer(recetas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecetasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecetasDetail(APIView):
    def get (self, request, pk):
        recetas = Recetas.objects.get(pk=pk)
        serializer = RecetasSerializer(recetas)
        return Response(serializer.data)
    def put (self, request, pk):
        recetas = Recetas.objects.get(pk=pk)
        serializer = RecetasSerializer(recetas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class RecetasDetailByName(APIView):
    def get (self, request, name):
        recetas = Recetas.objects.get(nombre=name)
        serializer = RecetasSerializer(recetas)
        return Response(serializer.data)

class RecetasDetailByTipo(APIView):
    def get (self, request, tipo):
        recetas = Recetas.objects.get(tipo=tipo)
        serializer = RecetasSerializer(recetas)
        return Response(serializer.data)