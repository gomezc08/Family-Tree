from django.shortcuts import render
from .models import Person

def index(request):
    members = Person.objects.all()
    return render(request, 'homescreen/index.html', {'members': members})