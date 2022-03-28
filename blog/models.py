from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
=======
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)

>>>>>>> origin/changrae


    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
