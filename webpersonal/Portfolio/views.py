from django.shortcuts import render
from .models import Project

def portfolio(request):
    project = Project.objects.all()
    return render(request,'portfolio/portfolio.html', {'projects' : project})
