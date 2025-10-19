from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name