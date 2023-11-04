import re

from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import AdvUser
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Повторите тот же самый пароль еще раз')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[а-яА-Я\s-]+$', name):
            raise ValidationError("ФИО может содержать только кириллицу, дефис и пробелы. ")
        return name

    def clean_login(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z\s-]+$', username):
            raise ValidationError("Логин может содержать только латиницу и дефис. ")
        if AdvUser.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже существует. ")
        return username

    class Meta:
        model = AdvUser
        fields = ('username', 'name', 'email', 'password1', 'password2')

