from django.shortcuts import render
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from rest_framework.viewsets import ModelViewSet
from course.models import Course
from rest_framework.response import Response
from users.models import User
from department.models import Department
from enrollment.models import Enrollment
from .serializers import AdminCourseSerializer,AdminStatSerializer,DepartmentStatSerializer,StudentStatSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class AdminCourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = AdminCourseSerializer

class AdminDashboardViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = AdminStatSerializer

    def list(self, request, *args, **kwargs):
        # Courses
        courses = Course.objects.all()
        total_course = courses.count()
        course_data = AdminStatSerializer(courses, many=True).data

        # Departments
        departments = Department.objects.all()
        total_departments = departments.count()
        department_data = DepartmentStatSerializer(departments, many=True).data

        # Students
        students = User.objects.filter(role='student')
        total_students = students.count()
        total_teachers = User.objects.filter(role='teacher').count()

        # Monthly sales
        monthly_sales = (
            Enrollment.objects
            .annotate(month=TruncMonth('enrolled_on'))
            .values('month')
            .annotate(total=Sum('course__price'))
            .order_by('month')
        )
        monthly_sales_data = [
            {"month": m['month'].strftime("%Y-%m"), "total_sales": m['total'] or 0} 
            for m in monthly_sales
        ]

        # Most purchased course
        most_purchased = (
            Enrollment.objects
            .values('course__id', 'course__title')
            .annotate(purchase_count=Count('id'))
            .order_by('-purchase_count')
            .first()
        )

        most_purchased_course = {
            "course_id": most_purchased['course__id'],
            "title": most_purchased['course__title'],
            "purchase_count": most_purchased['purchase_count']
        } if most_purchased else None

        dashboard_data = {
            "total_students": total_students,
            "total_teachers": total_teachers,
            "total_departments": total_departments,
            "total_course": total_course,
            "courses": course_data,
            "departments": department_data,
            "monthly_sales": monthly_sales_data,
            "most_purchased_course": most_purchased_course
        }

        return Response(dashboard_data)