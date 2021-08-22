from django.urls import include, path
from .views import RecipesAddView, RecipeView, RecipesView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('recipes/', RecipesView.as_view(), name='recipes'),
    path('recipe/<int:id>/', RecipeView.as_view(), name='recipe'),
    path('add-recipes/', RecipesAddView.as_view(), name='add-recipes'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
