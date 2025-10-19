from rest_framework import serializers
from .models import Enrollment
from course.serializers import CourseSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id','student','course','enrolled_on','progress','is_completed']

        read_only_fields = ['id', 'enrolled_on','progress','is_completed']