# Generated by Django 4.2.3 on 2023-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='image',
            field=models.ImageField(null=True, upload_to='dog_images/'),
        ),
    ]
