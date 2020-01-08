from rest_framework import viewsets
from .serializers import PlayerSerializer
from player.models import Player


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
