# Generated by Django 4.2.4 on 2023-09-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangogirls', '0011_alter_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.PositiveIntegerField(),
        ),
    ]
