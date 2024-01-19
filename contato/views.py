from django.shortcuts import render
from .forms import ContatoForm

# Create your views here.
def contato_form(request):
    form = ContatoForm()
    context = {
        'form': form
    }
    return render(request, 'contato/contato.html', context=context)