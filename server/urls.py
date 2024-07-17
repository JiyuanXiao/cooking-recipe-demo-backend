from django.urls import path
from .views import index, RecipeDetail, RecipeList, InstructionList, IngredientList

urlpatterns = [
    path('', index),
    path('recipes/', RecipeList.as_view()),
    path('recipe/<int:pk>/', RecipeDetail.as_view()),
    path('instruction/', InstructionList.as_view()),
    path('ingredient/', IngredientList.as_view()),
]