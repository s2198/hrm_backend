from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AnnualLeaveResetView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset-annual-leave/', AnnualLeaveResetView.as_view(), name='reset-annual-leave'),
]