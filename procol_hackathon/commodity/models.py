from django.db import models
from datetime import datetime

class Commodity(models.Model):
    commodity = models.CharField(max_length=30)
    sentiment = models.CharField(max_length=30)
    score = models.FloatField(max_length=30)
    created_at = models.DateTimeField()

    def __str__(self):
        string =  self.commodity + " " + self.created_at.strftime("%d-%m-%Y")
        return string 
