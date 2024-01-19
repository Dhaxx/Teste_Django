from django import forms 
from .models import Contato

class ContatoForm(forms.Form):
    class Meta:
        model = Contato
        fields = "__all__"