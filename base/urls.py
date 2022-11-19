from django.urls import path
from .views import getRoutes
from .views import getProducts
from .views import getProduct

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('products/', getProducts, name='products'),
    path('products/<str:pk>/', getProduct, name='product'),
]