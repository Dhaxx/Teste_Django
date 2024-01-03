from django.db import models

def upload_path(instance, filename):
    return f'projeto-imgs/{instance.titulo}/{filename}'

class Cidade(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    miniatura = models.ImageField(upload_to=upload_path, null=True, blank=True)
    tipo = models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=20, null=False, blank=False, default='residencial')

    titulo = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(null=False, blank=False)
    servicos_realizados = models.TextField(null=True, blank=True)

    imagem_cliente = models.ImageField(upload_to=upload_path, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    nome_cliente = models.CharField(max_length=100, null=False, blank=False)

    visivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
    class Meta():
        verbose_name_plural = 'Projetos'