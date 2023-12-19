from django.db import models

class Carrossel(models.Model):
    imagem = models.ImageField(upload_to='carrossel-imgs/%y/%m/', null=True, blank=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo + ' - ' + self.descricao
    
    class Meta:
        verbose_name_plural = 'carrosseis'