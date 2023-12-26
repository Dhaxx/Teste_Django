from django.shortcuts import render
from .models import Projetos

def expositor_projetos(request):
    projetos = Projetos.objects.all()
    return render(request, 'projetos/expositor_projetos.html', {'projetos': projetos})