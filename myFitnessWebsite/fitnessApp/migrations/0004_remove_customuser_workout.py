# Generated by Django 4.2.1 on 2023-05-29 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessApp', '0003_userworkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='workout',
        ),
    ]