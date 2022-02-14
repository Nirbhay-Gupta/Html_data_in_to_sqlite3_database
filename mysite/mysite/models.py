from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
   