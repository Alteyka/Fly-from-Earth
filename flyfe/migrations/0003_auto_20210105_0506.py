# Generated by Django 2.2.5 on 2021-01-05 05:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyfe', '0002_auto_20210105_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
