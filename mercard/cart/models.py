from django.db import models

# Create your models here.

class Cart(models.Model):
    client = models.CharField(max_length=120)
    lista = models.TextField()