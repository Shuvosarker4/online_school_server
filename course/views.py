from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from permission.permission import IsTeacher

# Create your views here.

class CourseViewSet(ModelViewSet):
    http_method_names =['get']
    queryset = Course.objects.all()
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
        return Course.objects.filter(teacher=self.request.user)