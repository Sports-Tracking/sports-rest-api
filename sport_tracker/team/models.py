from django.db import models

from sport.models import League


class Team(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    location = models.CharField(max_length=50, null=False)
    arena_name = models.CharField(max_length=50, null=False)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    coach = models.CharField(max_length=50, unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Team {self.name}>'
