from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField(default=0)
    password = models.CharField(max_length=6)