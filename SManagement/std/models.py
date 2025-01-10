from django.db import models

# Create your models here.

class Student(models.Model):
    regno = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)