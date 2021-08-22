from django.db import models


class DailyBalance(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    meals_names = models.TextField(blank=True, default='')
    total_calories = models.FloatField(blank=True, default=0)
    total_sugar = models.FloatField(blank=True, default=0)
    total_protein = models.FloatField(blank=True, default=0)
    total_fiber = models.FloatField(blank=True, default=0)
    total_potassium_mg = models.FloatField(blank=True, default=0)
    total_sodium_mg = models.FloatField(blank=True, default=0)
    total_fat_saturated = models.FloatField(blank=True, default=0)
    total_fat = models.FloatField(blank=True, default=0)
    total_carbohydrates = models.FloatField(blank=True, default=0)
    total_cholesterol_mg = models.FloatField(blank=True, default=0)
    user_diet = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        date = str(self.date).split()[0]
        return f"{date} {self.user_diet.username}"
