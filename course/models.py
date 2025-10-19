from django.db import models
from department.models import Department
from django.conf import settings
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='courses')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='courses')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.teacher}"
    
    class Meta:
        ordering = ['-created_at']
