from django.contrib.auth.models import Group, User
from django.shortcuts import render
from recipes.models import Recipe, RecipeType
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (GroupSerializer, RecipeSerializer,
                          RecipeTypeSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited. """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows groups to be viewed or edited. """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeViewSet(viewsets.ModelViewSet):
    """ API endpoint which allows recipes to be viewed and edited """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RecipeTypeViewSet(viewsets.ModelViewSet):
    """ API endpoint which shows recipe types """
    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer
    permission_classes = [permissions.AllowAny]
