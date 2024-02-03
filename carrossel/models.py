from django.db import models
from projetos.models import Projetos
from servicos.models import Servicos

class Carrossel(models.Model):
    titulo_carrossel = models.CharField(max_length=100, null=False, blank=False)
    projeto = models.ForeignKey(Projetos, on_delete=models.SET_NULL, null=True, blank=True)
    home = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo_carrossel

    class Meta:
        verbose_name_plural = 'carrosseis'

class ImagemCarrossel(models.Model):
    carrossel = models.ForeignKey(Carrossel, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='carrossel-imgs/%y/%m/', null=False, blank=False)
    titulo_imagem = models.CharField(max_length=100, null=False, blank=False)
    descricao_imagem = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.carrossel.titulo_carrossel} - {self.titulo_imagem}'

    class Meta:
        verbose_name_plural = 'imagens dos carrosseis'
