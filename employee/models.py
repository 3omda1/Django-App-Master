from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    email = models.EmailField()
    hire_date = models.DateField()

    def __str__(self):
        return self.full_name
