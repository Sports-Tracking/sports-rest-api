from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {}
    return render(request, 'soccer/index.html', context)

def premierleague(request):
    context = {}
    return render(request, 'soccer/premierleague.html', context)