from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)

def __str__(self):
    return 'Employee object with eno: +str(self.no)'