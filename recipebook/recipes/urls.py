from django.urls import path, include

from .views import *

#app_name = 'recipes'

urlpatterns = [
    path('', RecipeTypeListView.as_view(), name='index'),
    path('all/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('type/<int:pk>/', RecipeTypeDetailView.as_view(), name='recipetype-detail'),
]
