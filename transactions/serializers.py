from rest_framework import serializers
from .models import Product,Design,Cart


class DesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Design
        fields = ('url','name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Product
        fields= ('url','name','design')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Cart
        fields = ('url','customer_name','products')
