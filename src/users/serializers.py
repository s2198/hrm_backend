from django.contrib.auth.models import Group
from django.conf import settings
from django.db import transaction
from rest_framework import serializers
from .models import Employee, Project
from departments.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    is_head = serializers.BooleanField(read_only=True)

    class Meta:
        model = Department
        fields = ["id", "name", "is_head"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if "is_head" in self.context:
            ret["is_head"] = self.context["is_head"]
        return ret
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'role', 'duration', 'description']

class EmployeeSerializer(serializers.ModelSerializer):
    HR_ADMIN_EXCLUSIVE_FIELDS = [
        "employee_id",
        "email",
        "is_hr_admin",
        "start_date",
        "end_date",
        "job_title",
        "department_id",
        "is_head",
    ]
    is_hr_admin = serializers.BooleanField(write_only=False, required=False)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "last_name",
            "first_name",
            "email",
            "employee_id",
            "gender",
            "employment_status",
            "job_title",
            "phone_number",
            "start_date",
            "end_date",
            "is_hr_admin",
            "department",
            "skills",
            "certifications",
            "projects",
            "location",
            "mbti",
            "hobbies",
        ]

    def is_user_hr_admin(self):
        user = self.context["request"].user
        return user.groups.filter(name=settings.HR_ADMIN_GROUP_NAME).exists()

    @staticmethod
    def add_or_remove_hr_admin_group(is_hr_admin, user):
        if is_hr_admin is True:
            group = Group.objects.get(name=settings.HR_ADMIN_GROUP_NAME)
            group.user_set.add(user)
        elif is_hr_admin is False:
            group = Group.objects.get(name=settings.HR_ADMIN_GROUP_NAME)
            group.user_set.remove(user)

    def create(self, validated_data):
        projects_data = validated_data.pop('projects')
        is_hr_admin = validated_data.pop("is_hr_admin", False)
        with transaction.atomic():
            user = super().create(validated_data)
            self.add_or_remove_hr_admin_group(is_hr_admin, user)
            for project_data in projects_data:
                Project.objects.create(employee=user, **project_data)

        return user

    def update(self, instance, validated_data):
        projects_data = validated_data.pop('projects', None)
        if projects_data is not None:
            # 기존 프로젝트 삭제 및 새로운 프로젝트 생성
            instance.projects.all().delete()
            for project_data in projects_data:
                Project.objects.create(employee=instance, **project_data)

        # HR 관리자가 아닐 경우, HR 관리자 전용 필드 삭제
        if not self.is_user_hr_admin():
            for field in self.HR_ADMIN_EXCLUSIVE_FIELDS:
                validated_data.pop(field, None)

        is_hr_admin = validated_data.pop("is_hr_admin", None)
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            self.add_or_remove_hr_admin_group(is_hr_admin, instance)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["is_hr_admin"] = instance.groups.filter(
            name=settings.HR_ADMIN_GROUP_NAME
        ).exists()
        representation["employment_status"] = instance.get_employment_status_display()
        representation["gender"] = instance.get_gender_display()
        return representation
