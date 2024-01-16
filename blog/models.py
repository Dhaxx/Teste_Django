from django.db import models

def upload_path(instance, filename):
    return f'projeto-imgs/{instance.titulo}/{filename}'

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    imagem = models.ImageField(upload_to=upload_path, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    sobre = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Postagens'