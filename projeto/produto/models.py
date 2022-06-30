from django.db import models
from empresa.models import Empresa

class Produto(models.Model):
    nome = models.CharField( max_length=175)
    descricao = models.TextField()
    

    def __str__(self):
        return self.nome
    


class Produto_Empresa(models.Model):
    empresa = models.ForeignKey("empresa.Empresa", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.IntegerField()

    
