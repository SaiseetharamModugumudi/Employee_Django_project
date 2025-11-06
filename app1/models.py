from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField(default=15000)
    hire_date = models.DateTimeField(auto_now_add=True)