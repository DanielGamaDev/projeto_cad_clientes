from django.db import models

class Cliente(models.Model):
    nome = models.TextField(max_length=255)
    email = models.EmailField()
    razao = models.TextField(max_length=255)
    cnpj = models.IntegerField(primary_key=True)
    endereco = models.TextField(max_length=255)
    celular = models.IntegerField()