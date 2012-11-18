from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    clid = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
