from django.urls import path,include
from rest_framework_nested import routers
from department.views import DepartmentViewSet
from course.views import CourseViewSet

router = routers.DefaultRouter()
router.register('departments',DepartmentViewSet,basename='departments')
router.register('courses',CourseViewSet,basename='courses')

urlpatterns = [
   path('',include(router.urls)),
]