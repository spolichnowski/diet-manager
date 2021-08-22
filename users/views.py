from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.views import LoginView
from users.forms import RegistrationForm
from .models import CustomUser


class RegisterView(View):

    def get(self, request):
        return render(request, 'users/register.html', {"form": RegistrationForm})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("set-profile"))
        else:
            return redirect(reverse('register'))
        return redirect(reverse('register'))
