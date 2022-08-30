from django.db import models

# Create your models here.
class  Product(models.Model):
    name = models.TextField()
    prices = models.TextField()
    count = models.TextField(default="0")