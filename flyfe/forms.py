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

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
