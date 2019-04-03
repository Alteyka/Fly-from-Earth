from django import forms
from .models import Card
from django.core.exceptions import ValidationError

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
