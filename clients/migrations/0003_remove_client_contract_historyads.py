# Generated by Django 5.0.1 on 2024-01-09 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0001_initial"),
        ("clients", "0002_alter_client_name_alter_client_second_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="contract",
        ),
        migrations.CreateModel(
            name="HistoryAds",
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
                    "ads",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ads.ads",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="clients.client",
                    ),
                ),
            ],
        ),
    ]
