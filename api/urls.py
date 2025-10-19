from django.urls import path,include
from rest_framework_nested import routers
from department.views import DepartmentViewSet

router = routers.DefaultRouter()
router.register('departments',DepartmentViewSet,basename='departments')

urlpatterns = [
   path('',include(router.urls)),
]