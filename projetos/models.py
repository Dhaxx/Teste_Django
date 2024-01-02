from django.db import models

def upload_path(instance, filename):
    return f'projeto-imgs/{instance.titulo}/{filename}'

class Cidade(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    imagem_1 = models.ImageField(upload_to=upload_path, null=True, blank=True)
    imagem_2 = models.ImageField(upload_to=upload_path, null=True, blank=True)
    imagem_3 = models.ImageField(upload_to=upload_path, null=True, blank=True)
    imagem_4 = models.ImageField(upload_to=upload_path, null=True, blank=True)

    titulo = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=20, null=False, blank=False, default='residencial')

    sobre = models.CharField(max_length=350, null=False, blank=False)    

    imagem_cliente = models.ImageField(upload_to=upload_path, null=True, blank=True)
    feedback = models.CharField(max_length=150, null=False, blank=False)
    nome_cliente = models.CharField(max_length=100, null=False, blank=False)

    visivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
    class Meta():
        verbose_name_plural = 'Projetos'