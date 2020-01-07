from rest_framework import serializers
from player.models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'number']
