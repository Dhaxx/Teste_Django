from django.shortcuts import render
from .models import Projetos

def projetos_view(request):
    projetos = Projetos.objects.all()
    return render(request, 'projetos/projetos_template.html', {'projetos': projetos})