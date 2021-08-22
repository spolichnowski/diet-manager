from django import forms

SELECT_CATEGORY = 'empty'
BREAKFAST = 'BREAKFAST'
LUNCH = 'LUNCH'
DINNER = 'DINNER'
SNACK = 'SNACK'
OTHER = 'OTHER'
MEAL_OPTIONS = ((SELECT_CATEGORY, 'select category'), (BREAKFAST, 'breakfast'), (LUNCH, 'lunch'),
                (DINNER, 'dinner'), (SNACK, 'snack'), (OTHER, 'other'))


class AddIngredientsForm(forms.Form):
    ingredients = forms.CharField(max_length=254, required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Type food'}))


class SearchInput(forms.Form):
    recipe = forms.CharField(max_length=254, required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Search Recipe'}))
    category = forms.ChoiceField(required=True, choices=MEAL_OPTIONS, widget=forms.Select(
        attrs={'type': 'select', 'id': 'category', 'class': 'form-select', 'onChange': "form.submit();"}))
