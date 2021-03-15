from django import forms
from .models import MyUser


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5, max_length=80)
    password2 = forms.CharField()

    class Meta:
        model = MyUser
        fields = ['email','username', 'password', 'password2' ]
