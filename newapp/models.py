from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    number = models.IntegerField()
    password = models.CharField(max_length=15)
