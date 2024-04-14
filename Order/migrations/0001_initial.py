# Generated by Django 5.0.3 on 2024-04-14 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_creation_date",
                    models.DateTimeField(default=datetime.date.today),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("delivery_date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("canceled", "Canceled"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "verbose_name": "OrderItem",
                "verbose_name_plural": "OrderItem",
            },
        ),
    ]
