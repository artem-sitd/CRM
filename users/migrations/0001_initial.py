# Generated by Django 5.0.1 on 2024-01-07 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=40, null=True)),
                ("second_name", models.CharField(max_length=50, null=True)),
                ("surname", models.CharField(blank=True, max_length=40, null=True)),
                ("fired", models.BooleanField(blank=True, default=False, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "phone",
                    models.CharField(default="+0123456789", max_length=12, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
