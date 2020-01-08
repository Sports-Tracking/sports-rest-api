from rest_framework import viewsets
from .serializers import TeamSerializer
from team.models import Team


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
