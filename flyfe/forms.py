from django import forms
from .models import Card
from django.core.exceptions import ValidationError

class NewPlanetForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)
    body = forms.CharField(max_length=500)

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug =='create':
            raise ValidationError('Slug may not be "create"')
        return new_slug


    def save(self):
        new_planet = Card.objects.create(
        title=self.cleaned_data['title'],
        slug=self.cleaned_data['slug'],
        body=self.cleaned_data['text'])
        return new_planet
