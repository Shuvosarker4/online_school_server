from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Enrollment
from .serializers import EnrollmentSerializer
from permission.permission import IsStudent
from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EnrollmentViewSet(ModelViewSet):
    http_method_names =['post']
    permission_classes = [IsStudent]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
    

class StudentEnrollmentViewSet(ModelViewSet):
    http_method_names =['get']
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudent]
    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
    
    @action(detail=True, methods=['get'], url_path='progress')
    def progress(self, request, pk=None):
            try:
                enrollment = Enrollment.objects.get(student=request.user, course_id=pk)
            except Enrollment.DoesNotExist:
                return Response({'detail': 'Not enrolled in this course.'},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(enrollment)
            return Response({'course': enrollment.course.title, 'progress': serializer.data['progress'], 'is_completed': serializer.data['is_completed']})