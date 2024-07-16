from django.contrib import admin

from .models import Recipe, Instruction, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Instruction)   
admin.site.register(Ingredient)   