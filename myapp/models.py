from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpID=models.IntegerField()
    EmpName=models.CharField(max_length=40)
    EmpSal=models.IntegerField()

