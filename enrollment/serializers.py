from rest_framework import serializers
from .models import Enrollment
from course.serializers import CourseSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id','student','course','enrolled_on','progress','is_completed']

        read_only_fields = ['id', 'enrolled_on','progress','is_completed','student']

    def validate(self, attrs):
        user = self.context['request'].user
        course = attrs.get('course')

        if Enrollment.objects.filter(student=user, course=course).exists():
            raise serializers.ValidationError({'detail': 'You are already enrolled in this course.'})
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['student'] = user
        enroll = Enrollment.objects.create(**validated_data)
        return enroll