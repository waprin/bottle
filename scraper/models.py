from django.db import models

class CraigslistAd(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    cl_id = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    processed = models.BooleanField()

class CrushAd(models.Model):
    city = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    sc_id = models.CharField(max_length=50)
    processed = models.BooleanField()

