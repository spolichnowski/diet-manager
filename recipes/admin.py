from django.contrib import admin
from .models import Recipe, RecipeMacros

admin.site.register([Recipe, RecipeMacros])
