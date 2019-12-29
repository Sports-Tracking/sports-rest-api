from django.urls import path
from hockey import views
urlpatterns = [
    path('', views.index, name='index')
]
