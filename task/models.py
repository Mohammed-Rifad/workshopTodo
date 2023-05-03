from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date=models.CharField(max_length=20, default="")
    completion_date =models.CharField(max_length=20,default="not compleate")
    status=models.CharField(max_length=10,default="pending")
   