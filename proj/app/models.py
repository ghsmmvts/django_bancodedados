from django.db import models

# Create your models here.

# BANCO DE DADOS MODELS.MODEL
class Pessoa(models.Model):

    nome = models.CharField(max_length=255)
    # CHAR CAMPO DE LETRAS
    idade = models.IntegerField()
    # Numeros Inteiros o Integer

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
