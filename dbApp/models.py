from django.db import models

# Create your models here.
class Employee(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=20)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length=100)

def __str__(self):
    return 'Employee details are shared'
    