# Generated by Django 5.0.6 on 2024-06-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_employee_email_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="departmentuser",
            name="department",
        ),
        migrations.RemoveField(
            model_name="departmentuser",
            name="employee",
        ),
        migrations.DeleteModel(
            name="Department",
        ),
        migrations.DeleteModel(
            name="DepartmentUser",
        ),
    ]
