from django.shortcuts import render
from django.views.generic import ListView

from .models import Recipe

class RecipeListView(ListView):
    template_name = 'recipes/recipe_list.html'
    model = Recipe
