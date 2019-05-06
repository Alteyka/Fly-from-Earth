from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewPlanetForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['title', 'slug', 'body']

        # Bind forms with a bootstrap forms
        widgets = {'title': forms.TextInput(attrs={'class': 'form-conrol'}),
                   'slug': forms.TextInput(attrs={'class': 'form-conrol'}),
                   'body': forms.Textarea(attrs={'class': 'form-conrol'})}


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "create"')
        if Card.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {'password': forms.PasswordInput}

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
