from django import forms
from .models import Stats


class SetProfileForm(forms.Form):
    height = forms.FloatField(widget=forms.TextInput(
        attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Height'}))
    weight = forms.FloatField(widget=forms.TextInput(
        attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Weight'}))
    age = forms.IntegerField(widget=forms.TextInput(
        attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Age'}))


class AddStatsForm(forms.ModelForm):
    weight = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-weight', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    calf = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-calf', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    thigh = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-thigh', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    hips = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-hips', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    waist = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-waist', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    chest = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-chest', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    neck = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-neck', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    biceps = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-biceps', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))
    forearm = forms.FloatField(widget=forms.TextInput(
        attrs={'id': 'input-forearm', 'type': 'number', 'class': 'form-control', 'placeholder': '', 'value': '{{  }}'}))

    class Meta:
        model = Stats
        fields = [
            'weight',
            'calf',
            'thigh',
            'hips',
            'waist',
            'chest',
            'neck',
            'biceps',
            'forearm'
        ]
