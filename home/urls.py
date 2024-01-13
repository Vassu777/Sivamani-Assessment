# catalog/urls.py
from django.urls import path
from .views import ProductList, ProductDetail

app_name = 'home'
urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
