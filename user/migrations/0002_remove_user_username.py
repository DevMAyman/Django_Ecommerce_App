# Generated by Django 5.0.3 on 2024-04-08 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
