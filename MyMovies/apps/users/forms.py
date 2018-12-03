from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username","mobile","email","password"]

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username", "mobile", "email"]

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

