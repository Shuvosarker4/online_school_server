from django.db import models
from django.conf import settings
from course.models import Course

# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)
    is_completed = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    payment_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course.title}"

