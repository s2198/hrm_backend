from rest_framework import serializers
from .models import Employee, AnnualLeave
from .utils import calculate_annual_leave
from datetime import datetime, date, timedelta
class EmployeeSerializer(serializers.ModelSerializer):
    annual_leave_days = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'email', 'employee_id', 'start_date', 'annual_leave_days']

    def get_annual_leave_days(self, obj):
        today = datetime.today().date()
        year = today.year
        annual_leave = AnnualLeave.objects.filter(employee=obj, year=year).first()
        if annual_leave:
            return annual_leave.days
        return 0

class AnnualLeaveSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = AnnualLeave
        fields = ['id', 'employee', 'year', 'days']