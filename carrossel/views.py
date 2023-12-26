# views.py no app do carrossel
from django.shortcuts import render
from .models import Carrossel, ImagemCarrossel

def carrossel_view(request):
    carrosseis = Carrossel.objects.all()
    imagens = ImagemCarrossel.objects.all()
    return render(request, 'carrossel/carrossel_template.html', {'carrosseis': carrosseis, 'imagens': imagens})