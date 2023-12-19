from django.shortcuts import render
from carrossel.models import Carrossel

# Create your views here.
def index(request):
    home_carrossel = Carrossel.objects.all()
    return render(request, 'homes/index.html', {'home_carrossel': home_carrossel})