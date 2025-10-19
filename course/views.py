from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['department']
    search_fields = ['title']