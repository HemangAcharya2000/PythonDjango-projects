from django.db import models

# Create your models here.
class database(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    subject= models.TextField()
    
    def __str__(self):
        return self.name
    
