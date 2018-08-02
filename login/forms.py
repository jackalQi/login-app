from django import forms
from .models import User


class UserForm(forms.Form):
    # (attrs={'class':'form-control'})
    username = forms.CharField(max_length=128, label="username", widget=forms.TextInput)
    password = forms.CharField(max_length=256, label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    gender = (
        ("m", "male"),
        ("f", "female"),
    )

    username = forms.CharField(max_length=128, label="username", widget=forms.TextInput)
    password1 = forms.CharField(max_length=256, label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=256, label="password", widget=forms.PasswordInput)
    email = forms.EmailField(label="email", widget=forms.EmailInput)
    sex = forms.ChoiceField(label="sex", choices=gender)
