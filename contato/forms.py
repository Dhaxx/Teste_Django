from django import forms 

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    endereco = forms.CharField(max_length=120)
    assunto = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 8, 'class': 'form-subject;'}))