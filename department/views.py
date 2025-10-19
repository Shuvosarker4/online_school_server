from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
from permission.permission import IsAdminOrReadOnly
# Create your views here.

class DepartmentViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
