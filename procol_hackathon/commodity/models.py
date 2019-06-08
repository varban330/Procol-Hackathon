from django.db import models

class Commodity(models.Model):
    commodity = models.CharField(max_length=30)
    sentiment = models.CharField(max_length=30)
    score = models.CharField(max_length=30)
    time = models.DateField()
