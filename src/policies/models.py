from django.db import models
from django.contrib.auth.models import User
from users.models import Employee
from datetime import date, timedelta
from core.models import AbstractBaseModel

class AnnualLeave(AbstractBaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.IntegerField()
    days = models.IntegerField()

    class Meta:
        unique_together = ('employee', 'year')

    def __str__(self):
        return f"{self.employee.email} - {self.year}: {self.days} days"