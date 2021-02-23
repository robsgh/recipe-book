from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe
