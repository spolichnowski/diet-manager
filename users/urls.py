from django.urls import include, path
from django.contrib.auth.views import LoginView
from users.views import RegisterView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name="register"),

]
