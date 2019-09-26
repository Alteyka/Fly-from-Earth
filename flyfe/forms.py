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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    #first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    #                             max_length=32, help_text='First name')
    #last_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    #                            max_length=32, help_text='Last name')
    #email = forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,
    #                         help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)