from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# Function for generate slug based on linuxtime
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Card(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('card_detail_url', kwargs={'slug': self.slug})


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
