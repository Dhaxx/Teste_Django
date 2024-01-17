from django.shortcuts import render
from .models import Postagem, Categoria
from django.core.paginator import Paginator

# Create your views here.
def blog(request, categoria=None):
    if categoria:
        postagens = Postagem.objects.filter(categoria__nome=categoria)
    else:
        postagens = Postagem.objects.all()
    paginacao = Paginator(postagens, 6)
    page_num = request.GET.get('page')
    page = paginacao.get_page(page_num)

    categorias = Categoria.objects.all()

    return render(request, 'blog/blog.html', {'page': page, 'categorias': categorias})

def post_detalhado(request, titulo):
    post = Postagem.objects.get(titulo=titulo)
    
    return render(request, 'blog/post_detalhado.html', {'post': post})