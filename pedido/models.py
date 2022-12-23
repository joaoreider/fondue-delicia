
from django.db import models
from datetime import datetime
from produto.models import Produto

class Pedido(models.Model):
    usuario = models.CharField(max_length=200)
    total = models.FloatField()
    troco = models.CharField(blank=True, max_length=20)
    pagamento = models.CharField(max_length=20)
    ponto_referencia = models.CharField(max_length=2000, blank=True)
    data = models.DateTimeField(default=datetime.now())
    cep = models.CharField(max_length=50, blank=True)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=30)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    descricao = models.TextField()
    adicionais = models.TextField()