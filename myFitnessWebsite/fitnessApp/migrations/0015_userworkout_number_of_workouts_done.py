# Generated by Django 4.2.1 on 2023-06-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessApp', '0014_rename_height_customuser_calories_burned_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userworkout',
            name='number_of_workouts_done',
            field=models.PositiveIntegerField(null=True),
        ),
    ]