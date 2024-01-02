from django.shortcuts import render
from .models import Projetos
from django.core.paginator import Paginator

def expositor_projetos(request):
    projetos = Projetos.objects.filter(visivel=True)
    return render(request, 'projetos/expositor_projetos.html', {'projetos': projetos})

def projetos(request, tipo_projeto=None):
    if tipo_projeto:
        projetos = Projetos.objects.filter(tipo=tipo_projeto)
    else:
        projetos = Projetos.objects.all()

    paginacao = Paginator(projetos, 6)
    page_num = request.GET.get('page')
    page = paginacao.get_page(page_num)
        
    return render(request, 'projetos/projetos.html', {'page': page})

def projeto_detalhado(request, id):
    projeto = Projetos.objects.get(id=id)
    return render(request, 'projetos/projeto_detalhado.html', {'projeto': projeto})