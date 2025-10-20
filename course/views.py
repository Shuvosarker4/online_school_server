from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Course
from rest_framework.decorators import action
from .serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from permission.permission import IsTeacher
from enrollment.models import Enrollment
from users.serializers import SimpleStudentSerializer

# Create your views here.

class CourseViewSet(ModelViewSet):
    http_method_names =['get']
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['department']
    search_fields = ['title']

class TeacherCourseViewSet(ModelViewSet):
    # http_method_names =['get','put','patch','delete']
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Course.objects.none()
        return Course.objects.filter(teacher=self.request.user)
    
    @action(detail=True, methods=['get'], url_path='students')
    def students(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk, teacher=request.user)
        except Course.DoesNotExist:
            return Response({'detail': 'No Course Found'},
                            status=status.HTTP_404_NOT_FOUND)
        
        enrollments = Enrollment.objects.filter(course=course)
        students = [enrollment.student for enrollment in enrollments]
        serializer =SimpleStudentSerializer(students, many=True)
        return Response(serializer.data)