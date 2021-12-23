from django.db import models
from rest_framework import serializers

from .models import Shop

from product.serializers import ProductSerializer

class ShopSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Shop
        fields = (
            "id",
            "shopname",
            "addreess",
            "district",
            "state",
            "phone",
            "user",

            "products"
        )
    