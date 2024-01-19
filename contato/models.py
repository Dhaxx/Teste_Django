from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    endereco = models.CharField(max_length=120)
    assunto = models.TextField()

    def __str__(self):
        return self.nome