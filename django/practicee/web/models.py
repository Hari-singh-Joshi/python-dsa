from django.db import models

class MyModel(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()

