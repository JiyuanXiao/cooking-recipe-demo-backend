from django.db import models

# A model is a python class, represents a table in the db
# attrs are the fields in the table
# Create your models here.

class Recipe(models.Model):
    CATEGORY_CHOISES = [
        ("Rice", "Rice"),
        ("Noodle", "Noodle"),
        ("Entree", "Entree"),
        ("Baking", "Baking"),
        ("Hotpot", "Hotpot"),
        ("Soup", "Soup"),
        ("Drink", "Drink"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOISES)
    description = models.TextField()
    preparation_time = models.PositiveSmallIntegerField()
    cooking_time = models.PositiveSmallIntegerField()
    servings = models.PositiveSmallIntegerField(default=1)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

class Ingredient(models.Model):
    UNIT_CHOISES = [
        ("TEASPOON", "tsp"),
        ("TABLESPOON", "tbsp"),
        ("CUP", "cup"),
        ("PINT", "pt"),
        ("QUART", "quart"),
        ("GALLON", "gallon"),
        ("OUNCE", "oz"),
        ("FLUID OUNCE", "fl oz"),
        ("POUND", "lb"),
        ("MILLILITER", "mL"),
        ("LITER", "L"),
        ("GRAM", "g"),
        ("KILOGRAM", "kg"),
    ]
    ingredient = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit = models.CharField(max_length=15, choices=UNIT_CHOISES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredient")

    def __str__(self) -> str:
        return f"{self.recipe.name} | {self.ingredient}"

class Instruction(models.Model):
    step = models.PositiveSmallIntegerField()
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instruction")

    def __str__(self) -> str:
        return f"{self.recipe.name} | step {self.step}"