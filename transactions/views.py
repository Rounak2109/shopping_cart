from django.shortcuts import render
from rest_framework import viewsets,permissions
# Create your views here.
from .models import Product,Design,Cart
from .serializers import ProductSerializer,DesignSerializer,CartSerializer

class DesignView(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class= DesignSerializer
    #permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)

class ProductView(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class CartView(viewsets.ModelViewSet):
    queryset= Cart.objects.all()
    serializer_class=CartSerializer
