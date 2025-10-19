from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer