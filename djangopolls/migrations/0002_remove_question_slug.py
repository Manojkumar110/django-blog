# Generated by Django 4.2.3 on 2023-07-12 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopolls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
