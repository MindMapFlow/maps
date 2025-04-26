from django.db import models
from django.contrib.auth.models import User

class Major(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='roadmap_majors')

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=200)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='courses')
    semester = models.CharField(max_length=10, choices=[
        ('1-1', '1st Year, 1st Semester'),
        ('1-2', '1st Year, 2nd Semester'),
        ('1-3', '1st Year, 3rd Semester'),
        ('2-1', '2nd Year, 1st Semester'),
        ('2-2', '2nd Year, 2nd Semester'),
        ('2-3', '2nd Year, 3rd Semester'),
        ('3-1', '3rd Year, 1st Semester'),
        ('3-2', '3rd Year, 2nd Semester'),
        ('3-3', '3rd Year, 3rd Semester'),
    ])

    def __str__(self):
        return f"{self.name} ({self.major.name}, {self.semester})"