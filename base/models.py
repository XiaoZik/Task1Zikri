from django.db import models

class Notes(models.Model):

    author = models.CharField(max_length = 200)
    text = models.CharField(max_length = 2000)
    attachment = models.CharField(max_length=2000)

# Create your models here.
