from rest_framework import serializers
from course.models import Course
from users.models import User
from enrollment.models import Enrollment
from department.models import Department
from django.db.models import Sum, Count
# Create your models here.


class AdminCourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='teacher')
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'department',
            'teacher',
            'price',
            'is_active',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at',]


class DepartmentStatSerializer(serializers.ModelSerializer):
    total_courses = serializers.SerializerMethodField()
    total_enrollments = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            'id', 'name', 'total_courses', 'total_enrollments', 'total_sales'
        ]
        read_only_fields = fields

    def get_total_courses(self, obj):
        return Course.objects.filter(department=obj).count()

    def get_total_enrollments(self, obj):
        return Enrollment.objects.filter(course__department=obj).count()

    def get_total_sales(self, obj):
        total = Enrollment.objects.filter(course__department=obj).aggregate(
            total_sales=Sum('course__price')
        )['total_sales']
        return total or 0
    
    
class AdminStatSerializer(serializers.ModelSerializer):
    total_courses_by_teacher = serializers.SerializerMethodField()
    total_enrollments = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'title',
            'department',
            'teacher',
            'price',
            'is_active',
            'total_courses_by_teacher',
            'total_enrollments',
            'total_sales',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at','is_active','total_courses_by_teacher',
            'total_enrollments',
            'total_sales',]
    
    def get_total_courses_by_teacher(self, obj):
        return Course.objects.filter(teacher=obj.teacher).count()

    def get_total_enrollments(self, obj):
        return Enrollment.objects.filter(course=obj).count()

    def get_total_sales(self, obj):
        total = Enrollment.objects.filter(course=obj).aggregate(
            total_sales=Sum('course__price')
        )['total_sales']
        return total or 0
    

    
class StudentStatSerializer(serializers.ModelSerializer):
    total_enrollments = serializers.SerializerMethodField()
    total_courses_completed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'total_enrollments', 'total_courses_completed']
        read_only_fields = fields

    def get_total_enrollments(self, obj):
        return Enrollment.objects.filter(student=obj).count()

    def get_total_courses_completed(self, obj):
        return Enrollment.objects.filter(student=obj, is_completed=True).count()