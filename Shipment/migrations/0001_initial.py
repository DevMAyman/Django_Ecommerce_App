# Generated by Django 5.0.3 on 2024-04-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shipment",
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
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=10)),
                ("phone", models.CharField(max_length=15)),
            ],
            options={
                "verbose_name": "Shipment",
                "verbose_name_plural": "Shipments",
            },
        ),
    ]
