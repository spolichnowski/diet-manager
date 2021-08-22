from django import views
from django.shortcuts import redirect, render


def main_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
