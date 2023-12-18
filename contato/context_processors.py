from contato.forms import ContatoForm

def contato_form(request):
    return {'form_contato': ContatoForm()}