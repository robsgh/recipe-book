from django.contrib import admin

from .models import Recipe, RecipeType

admin.site.register(RecipeType)
admin.site.register(Recipe)
