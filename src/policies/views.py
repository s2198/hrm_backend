from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Employee, AnnualLeave
from .serializers import EmployeeSerializer, AnnualLeaveSerializer
from .utils import calculate_annual_leave
from datetime import datetime

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def calculate_leave(self, request, pk=None):
        employee = self.get_object()
        leave_days = calculate_annual_leave(employee)
        return Response({"employee_id": employee.id, "annual_leave_days": leave_days})

class AnnualLeaveResetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, version):
        today = datetime.today().date()
        year = today.year

        employees = Employee.objects.all()
        for employee in employees:
            leave_days = calculate_annual_leave(employee)
            annual_leave, created = AnnualLeave.objects.get_or_create(employee=employee, year=year)
            annual_leave.days = leave_days
            annual_leave.save()

        return Response({"message": "Annual leave reset successfully."}, status=status.HTTP_200_OK)