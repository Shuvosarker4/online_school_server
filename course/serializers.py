from rest_framework import serializers
from .models import Course
from users.serializers import UserSerializer
from department.serializers import DepartmentSerializer
class CourseSerializer(serializers.ModelSerializer):
    # teacher = UserSerializer()
    department = DepartmentSerializer()
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
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
