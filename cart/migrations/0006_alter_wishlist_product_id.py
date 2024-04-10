# Generated by Django 5.0.3 on 2024-04-04 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_auto_20240404_1357"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="product_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlists",
                to="products.product",
            ),
        ),
    ]