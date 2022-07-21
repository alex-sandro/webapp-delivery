from django.db import models


    class Cliente(models.Model):
        nome = models.CharField(max_length=30)
        endereco = models.CharField(max_length=250), verbose_name="endereço" #logradouro e número
        bairro = models.CharField(max_length=150)
        cidade = models.CharField(max_length=150)
        estado = models.CharField(max_length=2)
        cep = models.CharField(max_length=9)
        ponto_de_referencia = models.CharField(max_length=150)
        cpf = models.CharField(max_length=14)
        telefone = models.CharField(max_length=10)
