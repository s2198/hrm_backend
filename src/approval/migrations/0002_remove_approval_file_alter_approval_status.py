# Generated by Django 4.2 on 2024-07-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("approval", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="approval",
            name="file",
        ),
        migrations.AlterField(
            model_name="approval",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]
