from django import forms
from django.contrib.auth.models import User
from .models import *


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    soglasie = forms.BooleanField(label='Согласие на обработку персональных данных', widget=forms.BooleanField)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Поля паролей не совпадают!')
        return cd['password2']

    def soglasie(self):
        cd = self.cleaned_data
        if cd['soglasie'] != True:
            raise forms.ValidationError('Поле согласие на обработку персональных данных, обязательно!')
            return cd
        return cd['soglasie']


class RequestCreate(forms.ModelForm):

   #text = forms.CharField(label='Описание', widget=forms.Textarea)

    class Meta:
        model = Request
        fields = ('type', 'text', 'img')

