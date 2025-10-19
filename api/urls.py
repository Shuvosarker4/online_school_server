from django.urls import path,include
from rest_framework_nested import routers
from department.views import DepartmentViewSet
from course.views import CourseViewSet,TeacherCourseViewSet
from enrollment.views import EnrollmentViewSet
from enrollment.views import StudentEnrollmentViewSet
from dashboard.views import AdminCourseViewSet,AdminDashboardViewSet

router = routers.DefaultRouter()
router.register('departments',DepartmentViewSet,basename='departments')
router.register('courses',CourseViewSet,basename='courses')
router.register('teacher/courses',TeacherCourseViewSet,basename='teacher_courses')
router.register('student/enroll',EnrollmentViewSet,basename='enrolls')
router.register('student/enrollments',StudentEnrollmentViewSet,basename='student_enrollments')
router.register('admin/courses',AdminCourseViewSet,basename='admin_courses')
router.register('admin/dashboard',AdminDashboardViewSet,basename='admin_dashboard')

urlpatterns = [
   path('',include(router.urls)),
]