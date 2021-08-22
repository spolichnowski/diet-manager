from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib import messages
from .forms import RecipeForm
from diet.forms import SearchInput
from .models import Recipe, RecipeMacros
import requests


class RecipesView(View):

    def get(self, request):
        search_form = SearchInput()
        recipes = Recipe.objects.all()
        context = {
            'recipes': recipes,
            'search_form': search_form
        }
        return render(request, 'recipes/recipes.html', context)

    def post(self, request):
        search_form = SearchInput(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data.get('recipe')
            category = search_form.cleaned_data.get('category')
            if category == 'empty':
                print('empty')
                results = Recipe.objects.filter(name__contains=query)
            else:
                print('empty')
                results = Recipe.objects.filter(
                    name__contains=query,
                    category=category
                )
        context = {
            'search_form': search_form,
            'recipes': results,
        }
        return render(request, 'recipes/recipes.html', context)


class RecipesAddView(View):

    def get(self, request):
        recipe_form = RecipeForm()
        context = {
            'recipe_form': recipe_form,
            'username': request.user.username
        }
        return render(request, 'recipes/edit-recipes.html', context)

    def post(self, request):
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            ingredients = recipe_form.cleaned_data.get('ingredients')
            macros, _ = get_food(str(ingredients))
            calories = macros['calories']
            sugar = macros['sugar_g']
            protein = macros['protein_g']
            fiber = macros['fiber_g']
            potassium_mg = macros['potassium_mg']
            sodium_mg = macros['sodium_mg']
            fat_saturated = macros['fat_saturated_g']
            fat = macros['fat_total_g']
            carbohydrates = macros['carbohydrates_total_g']
            cholesterol_mg = macros['cholesterol_mg']

            macros = RecipeMacros(
                calories=calories,
                sugar=sugar,
                protein=protein,
                fiber=fiber,
                potassium_mg=potassium_mg,
                sodium_mg=sodium_mg,
                fat_saturated=fat_saturated,
                fat=fat,
                carbohydrates=carbohydrates,
                cholesterol_mg=cholesterol_mg
            )
            macros.save()
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.macros = macros
            recipe.save()
            messages.success(request, 'A new recipe has ben added.')

        return redirect(reverse('add-recipes'))


class RecipeView(View):

    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        return render(request, 'recipes/recipe.html', {'recipe': recipe})


def get_food(query):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        response = response.json()['items']
        print(response)
        ing = dict()
        ing_names = list()
        for e in response:
            print(e)
            for k, v in dict(e).items():
                print(k, v)
                if k == 'name':
                    ing_names.append(v)
                else:
                    ing[k] = ing.get(k, 0) + v
        return ing, ing_names
    else:
        print("Error:", response.status_code, response.text)


API_KEY = 'ybLTfcuuK7svgV3ecTldxQ==kkwHRB7vgaLYnt3l'
