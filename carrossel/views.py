# views.py no app do carrossel
from django.shortcuts import render
from .models import Carrossel

def carrossel_view(request):
    slides = Carrossel.objects.all()
    return render(request, 'carrossel/carrossel_template.html', {'slides': slides})
