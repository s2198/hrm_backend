# Generated by Django 5.0.6 on 2024-07-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0002_alter_notification_notification_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("to_do_assigned", "To Do Assigned"),
                    ("event_created", "Event Created"),
                    ("appointment_created", "Appointment Created"),
                ],
                max_length=30,
            ),
        ),
    ]
