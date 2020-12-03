from django.db import models

# Create your models here.


class Site(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_date = models.DateTimeField()