from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    subjects = models.CharField(max_length = 400)
    Grades = models.CharField(max_length = 200)
    usertype = "Teacher"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Grade = models.CharField(max_length = 2)
    roll_no = models.CharField(max_length = 8)
    address = models.CharField(max_length = 400)
    usertype = "Student"

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    usertype = "Staff"