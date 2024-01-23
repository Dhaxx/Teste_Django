from django.shortcuts import render
from .forms import ContatoForm

# Create your views here.
def contato_form(request):
    if request.method == 'GET':
        form = ContatoForm()
        context = {
            'form': form
        }
        return render(request, 'contato/contato.html', context=context)
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            form = ContatoForm()
            
        context = {
            'form': form
        }
        return render(request, 'contato/contato.html', context=context)
        