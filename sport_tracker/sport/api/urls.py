from django.urls import path, include
from .views import UserViewSet, LeagueViewSet, SoccerLeagueViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', LeagueViewSet)
router.register(r'users', UserViewSet)
router.register(r'soccer', SoccerLeagueViewSet)

urlpatterns = [
    path('', include(router.urls))
]
