from django.shortcuts import render
from .models import Challenge

# Create your views here.
def index(request):
    challenges = Challenge.objects.all()
    return render(request, 'index.html', {'challenges': challenges})
