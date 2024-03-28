from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Clothes
from .serializers import ClothesSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view
from .usecases import *

from rest_framework import viewsets, permissions, status
from .throttles import *


@api_view(["GET", "POST", "DELETE"])
def clothes_list(request):

    throttle_classes = [TenMinuteThrottle]
    if request.method == "GET":
        books = Clothes.objects.all()
        serializer = ClothesSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        Clothes.objects.all().delete()
        return Response({"detail": "All books deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ClothesViewSet(viewsets.ModelViewSet):
    queryset =Clothes.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = [permissions.IsAuthenticated]