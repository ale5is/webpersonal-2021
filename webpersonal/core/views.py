from django.shortcuts import render
import json

# Create your views here.
def home(request):
    nombre = 'Ale'
    apellido = 'Sa'
    owner_name = {
        'name' : nombre,
        'lastname' : apellido
    }
    return render(request, 'core/home.html', context=owner_name)

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')