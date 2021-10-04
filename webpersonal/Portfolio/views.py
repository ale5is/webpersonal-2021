from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import Project

# Create your views here.
def Portfolio(request):
    Project = Project.objects.all()
    return render(request,'core/Portfolio.html', {'Project' : Project})
