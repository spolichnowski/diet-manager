# Generated by Django 3.2.6 on 2021-08-22 13:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyCalories',
            new_name='DailyBalance',
        ),
    ]