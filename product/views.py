from django.shortcuts import render
from rest_framework import viewsets
from .models import category, brand, product
from rest_framework.response import Response

# Create your views here.

from .serializers import categorySerializer, brandSerializer, productSerializer

class categoryViewSet(viewsets.ViewSet):
    queryset = category.objects.all()
    
    def list(self, request):
        queryset = category.objects.all()
        serializer = categorySerializer(queryset, many=True)
        return Response(serializer.data)

class brandViewSet(viewsets.ViewSet):
    queryset = brand.objects.all()
    
    def list(self, request):
        queryset = brand.objects.all()
        serializer = brandSerializer(queryset, many=True)
        return Response(serializer.data)
    
class productViewSet(viewsets.ViewSet):
    queryset = product.objects.all()
    
    def list(self, request):
        queryset = product.objects.all()
        serializer = productSerializer(queryset, many=True)
        return Response(serializer.data)
