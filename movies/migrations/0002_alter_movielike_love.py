# Generated by Django 4.1.2 on 2022-11-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielike',
            name='love',
            field=models.BooleanField(default=True),
        ),
    ]
