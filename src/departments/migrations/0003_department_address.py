# Generated by Django 5.0.6 on 2024-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0002_alter_departmentuser_department"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="address",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
