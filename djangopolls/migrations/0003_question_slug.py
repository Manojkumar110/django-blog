# Generated by Django 4.2.3 on 2023-07-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangopolls', '0002_remove_question_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
