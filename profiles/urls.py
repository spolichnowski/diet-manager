from django.urls import include, path
from .views import DashboardView, ProfileView, SetProfileView, calorie_chart, weight_chart


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('set-profile/', SetProfileView.as_view(), name="set-profile"),
    path('dashboard/calorie_chart/', calorie_chart, name='calorie_chart'),
    path('dashboard/weight_chart/', weight_chart, name='weight_chart'),
]
