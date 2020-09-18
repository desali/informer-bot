from django import forms

from admins.models import Admin


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    fields = ['username', 'password']
