# Generated by Django 5.0.3 on 2024-04-12 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_remove_product_stripe_product_product_stripe_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="stripe_name",
        ),
    ]
