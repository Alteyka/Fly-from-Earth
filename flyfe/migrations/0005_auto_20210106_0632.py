# Generated by Django 2.2.5 on 2021-01-06 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyfe', '0004_auto_20210105_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
