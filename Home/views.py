from django.shortcuts import render
from carrossel.models import Carrossel, ImagemCarrossel
from servicos.models import Servicos
from projetos.models import Projetos

# Create your views here.
def index(request):
    home_carrossel = Carrossel.objects.all()
    imgs_carrossel = ImagemCarrossel.objects.all()
    home_servicos = Servicos.objects.all()
    projetos = Projetos.objects.filter(visivel=True)
    return render(request, 'homes/index.html', {'home_carrossel': home_carrossel, 'imagens': imgs_carrossel, 'home_servicos': home_servicos, 'projetos': projetos})