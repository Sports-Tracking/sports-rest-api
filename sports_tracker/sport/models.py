from django.db import models

# Create your models here.


class Player(models.Model):
    # pass
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    number = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Player {self.first_name} {self.last_name}>'


# sport -> league -> team -> players
#                         -> coach


# team i was in league j and had a win-loss ratio of p (differnt table)

# team is in a league
# user: generic
# password: root

# coach manager player (foeign key)
class Team(models.Model):
    # pass
    name = models.CharField(max_length=50, null=False, unique=True)
    location = models.CharField(max_length=50, null=False)
    arena_name = models.CharField(max_length=50, null=False)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    coach = models.CharField(max_length=50, unique=True)
    league = models.ForeignKey('League', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Team {self.name}>'

    # def get_win_loss_ration(self):
    #     return self.wins / self.losses
#


# class MatchHistory(models.Model):
#     pass


class League(models.Model):
    name = models.CharField(max_length=100)
