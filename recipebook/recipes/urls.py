from django.urls import path, include

from .views import *

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='list'),
]
