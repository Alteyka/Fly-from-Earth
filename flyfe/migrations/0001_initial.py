# Generated by Django 2.2.5 on 2021-01-11 11:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('grape', models.CharField(blank=True, max_length=200)),
                ('place', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=200)),
                ('year', models.DateField(blank=True, default=datetime.date.today)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
