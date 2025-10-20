from rest_framework import serializers
from .models import Course
from enrollment.models import Enrollment
from django.db.models import Sum, Count

class CourseSerializer(serializers.ModelSerializer):
    # teacher = UserSerializer()
    # department = DepartmentSerializer()
    total_sales = serializers.SerializerMethodField()
    image = serializers.ImageField()
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'department',
            'teacher',
            'image',
            'price',
            'is_active',
            'total_sales',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id','total_sales','created_at', 'updated_at','teacher']

    def get_total_sales(self, obj):
        total = Enrollment.objects.filter(course=obj).aggregate(
            total_sales=Sum('course__price')
        )['total_sales']
        return total or 0
    

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['teacher'] = user
        course = Course.objects.create(**validated_data)
        return course