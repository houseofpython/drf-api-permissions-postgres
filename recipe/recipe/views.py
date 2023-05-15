from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Recipe
from .serializer import RecipeSerializer
from .permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class RecipeList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Create your views here.
