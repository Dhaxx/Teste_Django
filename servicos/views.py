from django.shortcuts import render
from .models import Servicos

# Create your views here.
def servicos_view(request):
    servicos = Servicos.objects.all()
    return render(request, 'servicos/servicos.html', {'servicos': servicos})