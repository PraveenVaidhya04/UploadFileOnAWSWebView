from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))
    email = forms.EmailField(label="Email Address", max_length=254, help_text='Email.',widget=forms.TextInput(attrs={"placeholder": "E-mail"}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', )

