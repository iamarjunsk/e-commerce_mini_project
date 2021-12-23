from django.urls import path,include
from django.urls.resolvers import URLPattern

from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
    path('listcategories/', views.ListCategory.as_view()),
    path('products/search/',views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view()),
    path('add_product/',views.addProduct),
    path('seller-products/',views.SellerProducts),
    path('delete-product/<int:id>',views.productDelete),
]