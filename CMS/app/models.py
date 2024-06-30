from django.db import models
from django.contrib.auth.models import AbstractUser

# Extended Student model using AbstractUser from Django Allauth
class Student(AbstractUser):
    # Additional fields for the Student model
    address = models.TextField()
    phone_number = models.CharField(max_length=15,unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

# Professor model
class Professor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Professor {self.first_name} {self.last_name}"

# Course model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

# Enrollment model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return f"Enrollment: {self.student.username} in {self.course.course_name}"
