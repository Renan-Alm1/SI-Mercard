from django.db import models

# Create your models here.
class Entrance(models.Model):
    seller = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now=True)
    lista =  models.TextField()
