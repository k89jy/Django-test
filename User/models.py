from pyexpat import model
from statistics import mode
from django.db import models



class User(models.Model):
    nationality_english = "EN"
    nationality_korean = "KOR"
    nationality_choices = (
       (nationality_english, "EN"),
       (nationality_korean, "KOR"),
       
    )
    user_email = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    nationality = models.CharField( choices = nationality_choices, max_length=4)
    join_date = models.DateField(auto_now_add=True )
    leave_date = models.DateField(null=True )
    token = models.CharField(max_length=100)

