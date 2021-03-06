import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Function for generate slug based on linuxtime
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Card(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True)
    grape = models.CharField(max_length=200, blank=True)
    place = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    year = models.DateField(blank=True, default=datetime.date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    def get_absolute_url(self):
        return reverse('card_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('card_delete_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('card_update_url', kwargs={'slug': self.slug})

    # Redefinition function save() based on id.
    # If id is not defined card is not in DataBase.
    # The slug will be generated when creating the card, not when editing it.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
