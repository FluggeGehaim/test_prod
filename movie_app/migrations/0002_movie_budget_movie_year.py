# Generated by Django 5.0.2 on 2024-03-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
