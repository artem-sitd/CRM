# Generated by Django 5.0.1 on 2024-01-10 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0001_initial"),
        ("clients", "0003_remove_client_contract_historyads"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="ads",
            field=models.ForeignKey(
                default="ОБЯЗАТЕЛЬНО УКАЖИТЕ РЕКЛАМУ!",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ads.ads",
            ),
        ),
    ]
