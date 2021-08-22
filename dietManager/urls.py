from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import main_view


urlpatterns = [
    path('', main_view, name="main"),
    path('', include('users.urls')),
    path('', include('profiles.urls')),
    path('', include('recipes.urls')),
    path('', include('diet.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
