from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(max_length=254, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=254, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model = CustomUser
        fields = ("email", "username")

    def clean(self):
        password1 = self.cleaned_data.get('passoword1')
        password2 = self.cleaned_data.get('passoword2')
        if password1 != password2:
            raise ValidationError("Passwords must match!")
        return password1


class UserUpdateInfoForm(forms.Form):
    email = forms.EmailField(required=False, max_length=254, widget=forms.TextInput(
        attrs={'type': 'email', 'id': 'input-email', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'input-username', 'class': 'form-control', 'placeholder': 'Username'}))
