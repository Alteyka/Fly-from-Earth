from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewPlanetForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'grape', 'type', 'place', 'year', 'body', 'slug']

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "create"')
        if Card.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
