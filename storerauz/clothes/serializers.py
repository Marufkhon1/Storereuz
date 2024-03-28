from os import read
from unicodedata import lookup
from .models import *
from rest_framework import serializers






class ClothesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    brand = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    size = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=255)
    
    created = serializers.DateTimeField(read_only=True)
    author = serializers.CharField(max_length=255)

    class Meta:
        model = Clothes
        fields = '__all__'

