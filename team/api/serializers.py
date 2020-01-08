from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'location', 'arena_name', 'wins', 'ties', 'losses']
