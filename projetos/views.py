from django.shortcuts import render
from .models import Projetos
from django.core.paginator import Paginator

def expositor_projetos(request):
    projetos = Projetos.objects.filter(visivel=True)
    return render(request, 'projetos/expositor_projetos.html', {'projetos': projetos})

def projetos(request, tipo_projeto=None):
    if tipo_projeto:
        projetos = Projetos.objects.filter(tipo=tipo_projeto, visivel=True)
    else:
        projetos = Projetos.objects.filter(visivel=True)

    paginacao = Paginator(projetos, 6)
    page_num = request.GET.get('page')
    page = paginacao.get_page(page_num)
        
    return render(request, 'projetos/projetos.html', {'page': page})

def projeto_detalhado(request, titulo):
    projeto = Projetos.objects.get(titulo=titulo)
    projetos = Projetos.objects.filter(visivel=True).exclude(titulo=titulo)
    carrosseis_do_projeto = projeto.carrossel_set.all()

    imagens_do_projeto = []

    for carrossel in carrosseis_do_projeto:
        imagens_do_carrossel = carrossel.imagemcarrossel_set.all()
        
        imagens_do_projeto.extend(imagens_do_carrossel)

    return render(request, 'projetos/projeto_detalhado.html', {'projeto': projeto, 'carrossel': carrosseis_do_projeto, 'imagens_do_projeto':imagens_do_projeto, 'projetos':projetos})