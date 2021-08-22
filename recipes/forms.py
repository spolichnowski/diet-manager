from django import forms
from .models import Recipe

BREAKFAST = 'BREAKFAST'
LUNCH = 'LUNCH'
DINNER = 'DINNER'
SNACK = 'SNACK'
OTHER = 'OTHER'
MEAL_OPTIONS = ((BREAKFAST, 'breakfast'), (LUNCH, 'lunch'),
                (DINNER, 'dinner'), (SNACK, 'snack'), (OTHER, 'other'))


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=254, required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'recipe-name', 'class': 'form-control', 'placeholder': 'Recipe name'}))
    category = forms.ChoiceField(required=True, choices=MEAL_OPTIONS, widget=forms.Select(
        attrs={'type': 'select', 'id': 'category', 'class': 'form-select'}))
    photo = forms.ImageField(
        required=True, widget=forms.FileInput(attrs={'id': 'photo', 'type': 'file', 'class': 'custom-file-input zIndex'}))
    ingredients = forms.CharField(required=True,  widget=forms.Textarea(
        attrs={'type': 'text', 'id': 'ingredients', 'class': 'form-control', 'placeholder': 'Ingredients'}))

    class Meta:
        model = Recipe
        fields = ['name', 'category', 'photo', 'ingredients']
