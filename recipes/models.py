from django.db import models


class Recipe(models.Model):
    BREAKFAST = 'BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
    SNACK = 'SNACK'
    OTHER = 'OTHER'
    MEAL_OPTIONS = ((BREAKFAST, 'breakfast'), (LUNCH, 'lunch'),
                    (DINNER, 'dinner'), (SNACK, 'snack'), (OTHER, 'other'))

    name = models.CharField(max_length=254)
    category = models.CharField(choices=MEAL_OPTIONS, max_length=9)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    ingredients = models.TextField()
    macros = models.OneToOneField(
        "RecipeMacros", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecipeMacros(models.Model):
    calories = models.FloatField(blank=True, default=0)
    sugar = models.FloatField(blank=True, default=0)
    protein = models.FloatField(blank=True, default=0)
    fiber = models.FloatField(blank=True, default=0)
    potassium_mg = models.FloatField(blank=True, default=0)
    sodium_mg = models.FloatField(blank=True, default=0)
    fat_saturated = models.FloatField(blank=True, default=0)
    fat = models.FloatField(blank=True, default=0)
    carbohydrates = models.FloatField(blank=True, default=0)
    cholesterol_mg = models.FloatField(blank=True, default=0)
