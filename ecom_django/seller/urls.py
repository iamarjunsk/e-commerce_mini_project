from django.urls import path

from seller import views

urlpatterns = [
    path('add-shop/',views.add_shop),
    path('list-shops',views.ShopList.as_view()),
    path('list-place',views.PlaceList.as_view()),
]