from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe, Ingredient, Instruction
from .serializers import RecipeSerializer, IngredientSerializer, InstructionSerializer
from .utils import AddDataList, AddData

# Create your views here.
def index(request):
    return HttpResponse("<h1>Cooking Recipe Server</h1>")

class RecipeList(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        return AddData(request.data, RecipeSerializer)
    
class RecipeDetail(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        recipe = self.get_object(pk)
        ingredients = recipe.ingredient.all()
        instructions = recipe.instruction.all()
        ingredients_serializer = IngredientSerializer(ingredients, many=True)
        instructions_serializer = InstructionSerializer(instructions, many=True)
        recipe_dict = {
            "name" : recipe.name,
            "category": recipe.category,
            "description": recipe.description,
            "preparation_time" : recipe.preparation_time,
            "cooking_time" : recipe.cooking_time,
            "servings": recipe.servings,
            "likes" : recipe.likes,
            "ingredients" : ingredients_serializer.data,
            "instructions" : instructions_serializer.data, 
        }
        return Response(recipe_dict)
    
    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_200_OK)
    
class InstructionList(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            return AddDataList(request.data, InstructionSerializer)
        else:
            return AddData(request.data, InstructionSerializer)
    
class IngredientList(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            return AddDataList(request.data, IngredientSerializer)
        else:
            return AddData(request.data, IngredientSerializer)
