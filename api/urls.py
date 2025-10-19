from django.urls import path,include
from rest_framework_nested import routers
from department.views import DepartmentViewSet
from course.views import CourseViewSet,TeacherCourseViewSet
from enrollment.views import EnrollmentViewSet

router = routers.DefaultRouter()
router.register('departments',DepartmentViewSet,basename='departments')
router.register('courses',CourseViewSet,basename='courses')
router.register('enrollments',EnrollmentViewSet,basename='enrollments')
router.register('teacher/courses',TeacherCourseViewSet,basename='teacher_courses')

urlpatterns = [
   path('',include(router.urls)),
]