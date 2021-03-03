from django.urls import path, include

from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'recipe-types', views.RecipeTypeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]