# Generated by Django 3.2.21 on 2023-10-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio4', '0024_alter_comment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
