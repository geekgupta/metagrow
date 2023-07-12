
# Create your models here.
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    roll_number = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name
