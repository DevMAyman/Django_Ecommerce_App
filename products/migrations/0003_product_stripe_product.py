# Generated by Django 5.0.3 on 2024-04-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_auto_20240404_1406"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stripe_product",
            field=models.TextField(default="500", max_length=300),
        ),
    ]
