from django.db.models import Q
from django.http import Http404
from django.http.response import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from seller.models import Shop

from .models import Category, Product
from .serializers import ProductSerializer,CategorySerializer,CategoryListSerializer

class LatestProductList(APIView):
    def get(self, request, format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

# class SellerProducts(APIView):
#     @authentication_classes([authentication.TokenAuthentication])
#     @permission_classes([permissions.IsAuthenticated])
#     def get(self,request):
#         print(request.user)
#         # shop = Shop.objects.get(user = request.user)
#         # p = Product.objects.filter(shop=shop.id)
#         # serializer = ProductSerializer(p)
#         # return Response(serializer.data)r
#         return Response('hai')

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ListCategory(APIView):
    def get(self, request, format = None):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def addProduct(request):
    data = request.data
    shop = Shop.objects.get(user=request.user)
    # print(shop.shopname)
    productslug = data.get('productname')
    productslug = productslug.replace(" ", "_")
    category = Category.objects.get(slug=data.get('category'))
    product = Product(
        shop = shop,
        name = data.get('productname'),
        slug = productslug,
        description = data.get('discription'),
        price = data.get('price'),
        gender = data.get('gender'),
        category=category,
        image = data.get('image')
    )
    product.save()
    # print(request.user)
    
    # print(request.FILES['image'])
    return Response({"status" : "success"})

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def SellerProducts(request):
    shop = Shop.objects.get(user = request.user)
    p = Product.objects.filter(shop=shop.id)
    # print(p)
    serializer = ProductSerializer(p,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def productDelete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    shop = Shop.objects.get(user = request.user)
    p = Product.objects.filter(shop=shop.id)
    # print(p)
    serializer = ProductSerializer(p,many=True)
    return Response(serializer.data)