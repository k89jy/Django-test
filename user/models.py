from django.db import models
class User(models.Model):
    username    = models.CharField(max_length = 100)
    email       = models.CharField(max_length = 200)
    phonenum    = models.CharField(max_length = 100,blank=True)
    password    = models.CharField(max_length = 500)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "users"