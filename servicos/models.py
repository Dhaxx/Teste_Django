from django.db import models

def upload_path(instance, filename):
    return f'servicos-imgs/{instance.titulo}/{filename}'

class Servicos(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    imagem = models.ImageField(upload_to=upload_path, null=True, blank=True)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta():
        verbose_name_plural = 'Servicos'