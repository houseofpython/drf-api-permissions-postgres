from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'description', 'ingredients', 'updated_at')
        model = Recipe
