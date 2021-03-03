from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe, RecipeType

class RecipeTypeListView(ListView):
    model = RecipeType

class RecipeListView(ListView):
    model = Recipe

class RecipeTypeDetailView(DetailView):
    model = RecipeType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = self.get_object().get_recipes()
        return context

class RecipeDetailView(DetailView):
    model = Recipe
