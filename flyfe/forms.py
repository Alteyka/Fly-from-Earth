from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewPlanetForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['title', 'slug', 'body']

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "create"')
        if Card.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug


class LoginForm(forms.ModelForm):

    class Meta:
        model = User

        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

        widgets = {'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'})
                   }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']


        if commit:
            user.save()

        return user
