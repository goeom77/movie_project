# Generated by Django 3.2.15 on 2022-10-13 06:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0005_movie_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='like_user',
        ),
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movie', to=settings.AUTH_USER_MODEL),
        ),
    ]
