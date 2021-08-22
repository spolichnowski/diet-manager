from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, Stats
from .forms import AddStatsForm, SetProfileForm
from diet.models import DailyBalance
from users.forms import UserUpdateInfoForm
from users.models import CustomUser

from datetime import date, datetime, timedelta


@login_required
def calorie_chart(request):
    weekly_balance = DailyBalance.objects.filter(
        user_diet=request.user).order_by('date')[0:7]
    labels = [e.date.strftime('%A') for e in weekly_balance]
    data = [e.total_calories for e in weekly_balance]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def weight_chart(request):
    user_profile = Profile.objects.get(user=request.user)
    stats = Stats.objects.filter(
        user_profile=user_profile).order_by('date')[0:10]
    labels = [e.date.strftime("%d/%m/%Y") for e in stats]
    data = [e.weight for e in stats]

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


class SetProfileView(LoginRequiredMixin, View):

    def get(self, request):
        profile_form = SetProfileForm()
        return render(request, 'profiles/set-profile.html', {'profile_form': profile_form})

    def post(self, request):
        profile_form = SetProfileForm(request.POST)
        if profile_form.is_valid():
            height = profile_form.cleaned_data.get('height')
            weight = profile_form.cleaned_data.get('weight')
            age = profile_form.cleaned_data.get('age')
            initial_profile = Profile(
                user=request.user,
                height=height,
                age=age
            )
            initial_profile.save()
            initial_stats = Stats(user_profile=initial_profile, weight=weight)
            initial_stats.save()
            return redirect(reverse("dashboard"))


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        today = date.today()
        try:
            daily_balance = DailyBalance.objects.get(
                date=today, user_diet=request.user)
        except:
            daily_balance = DailyBalance(user_diet=request.user)

        profile = Profile.objects.get(user=request.user)
        stats = Stats.objects.filter(user_profile=profile).order_by('-date')
        profile.bmi = calc_bmi(stats[0].weight, profile.height)
        profile.bmr = calc_bmr(
            stats[0].weight,
            profile.height,
            profile.age,
            request.user.sex
        )
        profile.save()

        context = {
            'username': request.user.username,
            'profile': profile,
            'stats': stats,
            'calories': daily_balance.total_calories,
        }

        return render(
            request,
            'profiles/dashboard.html',
            context
        )


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        update_user_form = UserUpdateInfoForm()
        add_stats_form = AddStatsForm()
        profile_form = SetProfileForm()
        profile = Profile.objects.get(user=request.user)
        stats = Stats.objects.filter(user_profile=profile)
        profile.bmi = calc_bmi(stats[0].weight, profile.height)
        profile.bmr = calc_bmr(
            stats[0].weight,
            profile.height,
            profile.age,
            request.user.sex
        )
        profile.save()

        context = {
            'profile_form': profile_form,
            'profile': profile,
            'user': request.user,
            'add_stats_form': add_stats_form,
            'update_user_form': update_user_form
        }

        return render(
            request,
            'profiles/profile.html',
            context
        )

    def post(self, request):
        add_stats_form = AddStatsForm(request.POST)
        update_user_form = UserUpdateInfoForm(request.POST)
        set_profile_form = SetProfileForm(request.POST)
        profile = Profile.objects.get(user=request.user)
        if set_profile_form.is_valid():
            profile.height = set_profile_form.cleaned_data.get('height')
            profile.age = set_profile_form.cleaned_data.get('age')
            profile.save()
            messages.success(
                request,
                'Your profile information has been updated.'
            )

        elif add_stats_form.is_valid():
            profile = Profile.objects.get(user=request.user)
            stats = add_stats_form.save(commit=False)
            stats.user_profile = profile
            stats.save()
            messages.success(
                request,
                'New stats has been added.'
            )

        elif update_user_form.is_valid():
            username = update_user_form.cleaned_data.get('username')
            email = update_user_form.cleaned_data.get('email')
            user = CustomUser.objects.get(id=request.user.id)
            if username:
                user.username = username
            if email:
                user.email = email
            user.save()
            messages.success(
                request,
                'User information has been updated.'
            )
        return redirect(reverse("profile"))


def calc_bmi(weight, height):
    return weight / ((height/100)**2)


def calc_bmr(weight, height, age, sex):
    bmr = (10*weight)+(6.25*height)-(5*age)
    if sex == "Male":
        return bmr + 5
    else:
        return bmr - 161
