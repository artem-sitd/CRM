# Generated by Django 5.0.1 on 2024-01-07 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                ("title", models.CharField(max_length=50)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("archived", models.BooleanField(default=False)),
                (
                    "description",
                    models.CharField(db_index=True, max_length=500, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("validity", models.DateTimeField(null=True)),
                ("file", models.FileField(null=True, upload_to="contracts/file")),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
