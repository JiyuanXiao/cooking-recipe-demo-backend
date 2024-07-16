from django.urls import path
from .views import index, get_recipe, get_recipe_list

urlpatterns = [
    path('', index),
    path('recipes/', get_recipe_list),
    path('recipe/<int:pk>/', get_recipe),
]