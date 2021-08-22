from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import DailyBalance
from .forms import AddIngredientsForm, SearchInput
from recipes.models import Recipe

from datetime import date
from decouple import config
import requests


@login_required
def add_recipe_to_diet(request, id):
    today = date.today()
    recipe = Recipe.objects.get(id=id)

    recipe_m = recipe.macros
    daily_balance = DailyBalance.objects.get(
        user_diet=request.user, date=today)
    daily_balance.meals_names += ''.join(recipe.ingredients)
    daily_balance.total_calories += recipe_m.calories
    daily_balance.total_sugar += recipe_m.sugar
    daily_balance.total_protein += recipe_m.protein
    daily_balance.total_fiber += recipe_m.fiber
    daily_balance.total_potassium_mg += recipe_m.potassium_mg
    daily_balance.total_sodium_mg += recipe_m.sodium_mg
    daily_balance.total_fat_saturated += recipe_m.fat_saturated
    daily_balance.total_fat += recipe_m.fat
    daily_balance.total_carbohydrates += recipe_m.carbohydrates
    daily_balance.total_cholesterol_mg += recipe_m.cholesterol_mg
    daily_balance.save()
    messages.success(request, 'Your daily balance has been updated.')
    return redirect(reverse('diet'))


class DietView(LoginRequiredMixin, View):

    def get(self, request):
        search_form = SearchInput()
        ingredients_form = AddIngredientsForm()
        today = date.today()
        try:
            daily_balance = DailyBalance.objects.get(
                user_diet=request.user, date=today)
        except:
            daily_balance = DailyBalance(user_diet=request.user)
            daily_balance.save()

        context = {
            'ingredients_form': ingredients_form,
            'balance': daily_balance,
            'username': request.user.username,
            'search_form': search_form
        }
        return render(
            request,
            'diet/diet.html',
            context
        )

    def post(self, request):
        search_form = SearchInput(request.POST)
        ingredients_form = AddIngredientsForm(request.POST)
        today = date.today()
        try:
            daily_balance = DailyBalance.objects.get(
                user_diet=request.user, date=today)
        except:
            daily_balance = DailyBalance(user_diet=request.user)
            daily_balance.save()

        if search_form.is_valid():
            query = search_form.cleaned_data.get('recipe')
            category = search_form.cleaned_data.get('category')
            if category == 'empty':
                results = Recipe.objects.filter(
                    name__contains=query,
                )
            else:
                results = Recipe.objects.filter(
                    name__contains=query,
                    category=category
                )

        elif ingredients_form.is_valid():
            today = date.today()
            daily_balance = DailyBalance.objects.get(
                user_diet=request.user, date=today)
            ingredients = ingredients_form.cleaned_data.get('ingredients')

            try:
                macros, names = get_macros(str(ingredients))
                daily_balance.meals_names += ''.join(names)
                daily_balance.total_calories += macros['calories']
                daily_balance.total_sugar += macros['sugar_g']
                daily_balance.total_protein += macros['protein_g']
                daily_balance.total_fiber += macros['fiber_g']
                daily_balance.total_potassium_mg += macros['potassium_mg']
                daily_balance.total_sodium_mg += macros['sodium_mg']
                daily_balance.total_fat_saturated += macros['fat_saturated_g']
                daily_balance.total_fat += macros['fat_total_g']
                daily_balance.total_carbohydrates += macros['carbohydrates_total_g']
                daily_balance.total_cholesterol_mg += macros['cholesterol_mg']
                daily_balance.save()
                messages.success(
                    request, 'Ingredient has ben added.')
            except:
                messages.error(
                    request, 'Something went wrong! Try again later.')

            return redirect(reverse('diet'))

        context = {
            'ingredients_form': ingredients_form,
            'balance': daily_balance,
            'username': request.user.username,
            'search_form': search_form,
            'recipes': results
        }

        return render(
            request,
            'diet/diet.html',
            context
        )


def get_macros(query):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(
        api_url + query, headers={'X-Api-Key': config('API_KEY')})
    if response.status_code == requests.codes.ok:
        response = response.json()['items']
        ing = dict()
        ing_names = list()
        for e in response:
            for k, v in dict(e).items():
                if k == 'name':
                    ing_names.append(v)
                else:
                    ing[k] = ing.get(k, 0) + v
        return ing, ing_names
    else:
        print("Error:", response.status_code, response.text)
