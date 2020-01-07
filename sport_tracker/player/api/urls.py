from django.urls import path, include
from .views import PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
