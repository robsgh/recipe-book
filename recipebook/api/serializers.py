from django.contrib.auth.models import User, Group

from rest_framework import serializers

from recipes.models import Recipe, RecipeType

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = serializers.ListField(required=False)
    steps = serializers.ListField(required=False)

    class Meta:
        model = Recipe
        exclude = ['ingredients_json', 'steps_json']

class RecipeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeType
        exclude = ['slug']
