from django.urls import path
from soccer import views
urlpatterns = [
    path('', views.index, name='index'),
    path('premierleague', views.premierleague, name='pl')
]
