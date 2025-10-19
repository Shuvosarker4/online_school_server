from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    ROLES = (
        ("teacher", "Teacher"),
        ("student", "Student"),
    )
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=20,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=20,choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} by {self.email}"

