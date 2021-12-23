from abc import abstractmethod
from django.shortcuts import render
from django.db.models import Q
from rest_framework import serializers
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShopSerializer
from .models import Shop
# Create your views here.


@api_view(['POST']) 
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def add_shop(request):
    # serializer = ShopSerializer(data=request.data)
    # if serializer.is_valid():
    #     try:
    #         serializer.save()

    shop = Shop(
            shopname = request.data.get('shopname'),
            user = request.user,
            addreess=request.data.get('address'),
            district=request.data.get('district'),
            state = request.data.get('state'),
            phone = request.data.get('phone')
            )
    shop.save()
    return Response('Hai')

class ShopList(APIView):
    def get(self, request, format = None):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops,many=True)
        return Response(serializer.data)
    
class PlaceList(APIView):
    def get(self,request):
        print(request.GET.get('place'))
        shops = Shop.objects.filter(Q(district__icontains=request.GET.get('place')))
        # print(shops)
        # return Response('j')
        serializers = ShopSerializer(shops,many=True)
        return Response(serializers.data)