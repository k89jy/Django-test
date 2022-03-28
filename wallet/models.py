from django.db import models

# Create your models here.

class wallet(models.Model):
    krw  = models.IntegerField()
    btc  = models.IntegerField()
    eht  = models.IntegerField()
    ustd = models.IntegerField()

