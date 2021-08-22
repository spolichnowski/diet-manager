from django.contrib import admin
from .models import Profile, Stats


admin.site.register([Profile, Stats])
