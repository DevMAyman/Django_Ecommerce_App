# Generated by Django 5.0.3 on 2024-04-12 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Order", "0001_initial"),
        ("Shipment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Shipment.shipment"
            ),
        ),
    ]
