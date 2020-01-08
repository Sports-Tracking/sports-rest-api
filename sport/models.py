from django.db import models


class League(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'< {self.slug} - {self.name}>'
