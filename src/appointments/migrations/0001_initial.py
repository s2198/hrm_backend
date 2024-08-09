# Generated by Django 5.0.6 on 2024-07-09 13:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("departments", "0004_department_head_delete_departmentuser"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("new_job_title", models.CharField(max_length=100)),
                ("is_department_head", models.BooleanField(default=False)),
                ("effective_date", models.DateField(default=django.utils.timezone.now)),
                ("note", models.TextField(blank=True, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="appointments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "new_department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="appointments",
                        to="departments.department",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
