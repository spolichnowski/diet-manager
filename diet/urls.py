from django.urls import include, path
from .views import DietView, add_recipe_to_diet


urlpatterns = [
    path('diet/', DietView.as_view(), name='diet'),
    path('diet/<int:id>/', add_recipe_to_diet, name='add_recipe_to_diet')
]
