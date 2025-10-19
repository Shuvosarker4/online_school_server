from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
# Create your views here.

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
