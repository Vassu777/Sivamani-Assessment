# catalog/urls.py
from django.urls import path
from .views import ProductList, ProductDetail,Users,UserDetail

app_name = 'home'
urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('users/',Users.as_view(), name = 'user-list'),
    path('users/<int:pk>/',UserDetail.as_view(), name = 'user-detail')
]
