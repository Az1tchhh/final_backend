# Generated by Django 5.1.4 on 2024-12-08 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_webuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='webuser',
            name='password',
        ),
    ]
