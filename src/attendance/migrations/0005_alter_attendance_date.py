# Generated by Django 5.0.6 on 2024-07-02 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0004_alter_attendance_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
