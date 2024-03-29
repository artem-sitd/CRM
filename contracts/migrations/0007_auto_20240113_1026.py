# Generated by Django 5.0.1 on 2024-01-13 05:26

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0006_auto_20240113_1026"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="uniq_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
