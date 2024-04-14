from django.db import models

# Create your models here.
class Mobile(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)