# Generated by Django 4.1.2 on 2022-11-03 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movielike_love'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movielike',
            old_name='like',
            new_name='user',
        ),
    ]
