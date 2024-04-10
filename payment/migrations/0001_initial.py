# Generated by Django 5.0.3 on 2024-04-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("payment_bool", models.BooleanField(default=False)),
                ("stripe_checkout_id", models.CharField(max_length=500)),
            ],
        ),
    ]
