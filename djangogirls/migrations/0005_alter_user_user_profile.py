# Generated by Django 4.2.3 on 2023-07-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangogirls', '0004_alter_user_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(blank=True, null=True, upload_to='avtar'),
        ),
    ]
