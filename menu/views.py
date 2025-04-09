from django.shortcuts import render
from .models import MenuItem
from rest_framework import viewsets
from .serializers import MenuItemSerializers


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
