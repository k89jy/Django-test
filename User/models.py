from pyexpat import model
from statistics import mode
from django.db import models



class User(models.Model):


    user_email = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    confirm_password = models.CharField(max_length=100)

    nationality = models.CharField(max_length=100)

    join_date = models.CharField(max_length=100)

    leave_date = models.CharField(max_length=100)

