# Generated by Django 3.2.21 on 2023-10-04 21:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio4', '0013_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
