

# Create your models here.
#models 
from django.db import models

# Create your models here.
class Codebin(models.Model):
    
    pastetitle = models.CharField(max_length=20)
    pastecontent = models.TextField(max_length=900)
    sid = models.IntegerField()

# string function
    def __str__(self):
        return self.pastetitle



