from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    height = models.FloatField(blank=True, default=0)
    age = models.IntegerField(blank=True, default=0)
    bmi = models.FloatField(blank=True, default=0)
    bmr = models.FloatField(blank=True, default=0)
    water_demand = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f'{self.user.username}'


class Stats(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    weight = models.FloatField(blank=True, default=0)
    calf = models.FloatField(blank=True, default=0)
    thigh = models.FloatField(blank=True, default=0)
    hips = models.FloatField(blank=True, default=0)
    waist = models.FloatField(blank=True, default=0)
    chest = models.FloatField(blank=True, default=0)
    neck = models.FloatField(blank=True, default=0)
    biceps = models.FloatField(blank=True, default=0)
    forearm = models.FloatField(blank=True, default=0)
    user_profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        date = str(self.date).split()[0]
        return f'{self.user_profile.user.username} {date}'

    class Meta:
        verbose_name = "Stats"
        verbose_name_plural = "Stats"
