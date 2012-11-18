from django.db import models

class Description(models.Model):
    email = models.CharField(max_length=50)
    height = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10)
    hair_length = models.CharField(max_length=10)
    race = models.CharField(max_length=10)
    eyes = models.CharField(max_length=20)
    tone = models.CharField(max_length=50)
