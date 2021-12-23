from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class LatestProductList(APIView):
    def get(self, request, format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request, format = None):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        print(serializer.data['products'])
        return Response(serializer.data)