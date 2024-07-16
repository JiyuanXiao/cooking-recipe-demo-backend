from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Recipe, Ingredient, Instruction
from .serializers import RecipeSerializer, IngredientSerializer, InstructionSerializer

# Create your views here.
def index(request):
    return HttpResponse("<h1>Cooking Recipe Server</h1>")

def get_recipe(request, pk):
    if request.method == 'GET':
        # recipe = Recipe.objects.get(pk=pk)
        recipe = get_object_or_404(Recipe, pk=pk)
        ingredients = recipe.ingredient.all()
        instructions = recipe.instruction.all()

        ingredients_serializer = IngredientSerializer(ingredients, many=True);
        instructions_serializer = InstructionSerializer(instructions, many=True);

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
        return JsonResponse({"recipe" : recipe_dict})
    else:
        return HttpResponse(status=400)

def get_recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipe_list = []
        for recipe in recipes:
            ingredients = recipe.ingredient.all()
            instructions = recipe.instruction.all()
            ingredients_serializer = IngredientSerializer(ingredients, many=True);
            instructions_serializer = InstructionSerializer(instructions, many=True);
            recipe_list.append({
                "name" : recipe.name,
                "category": recipe.category,
                "description": recipe.description,
                "preparation_time" : recipe.preparation_time,
                "cooking_time" : recipe.cooking_time,
                "servings": recipe.servings,
                "likes" : recipe.likes,
                "ingredients" : ingredients_serializer.data,
                "instructions" : instructions_serializer.data,
            })

        return JsonResponse(recipe_list, safe=False)
    else:
        return HttpResponse(status=400)

# def ingredient_list(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     ingredients = recipe.ingredient.all()
#     ingredients_serializer = IngredientSerializer(ingredients, many=True);
#     return JsonResponse(ingredients_serializer.data, safe=False)

# def instruction_list(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     instructions = recipe.instruction.all()
#     instruction_serializer = InstructionSerializer(instructions, many=True);
#     return JsonResponse(instruction_serializer.data, safe=False)