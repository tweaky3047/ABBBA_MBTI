# Generated by Django 4.1.2 on 2022-11-03 11:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_alter_movie_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
