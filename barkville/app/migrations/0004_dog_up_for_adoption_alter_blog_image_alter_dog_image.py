# Generated by Django 4.2.3 on 2023-07-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='up_for_adoption',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dog_images/'),
        ),
    ]
