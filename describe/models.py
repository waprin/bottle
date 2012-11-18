from django.db import models

class Description(models.Model):
    height = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    eyes = models.CharField(max_length=20)
    skin = models.CharField(max_length=50)

    
