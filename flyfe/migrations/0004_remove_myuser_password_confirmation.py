# Generated by Django 2.1.7 on 2019-05-09 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyfe', '0003_auto_20190507_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='password_confirmation',
        ),
    ]