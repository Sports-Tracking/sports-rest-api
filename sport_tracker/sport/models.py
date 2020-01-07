from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    sport = models.CharField(max_length=100)
