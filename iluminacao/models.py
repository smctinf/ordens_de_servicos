from tabnanny import verbose
from django.db import models

# Create your models here.

class OrdemDeServico(models.Model):

    id=models.CharField(max_lenght=130)
    logradouro=models.CharField(max_lenght=150, verbose_name='Logradouro')
    referencia=models.CharField(max_lenght=150, verbose_name='Referência', blank=True)
    motivo_reclamacao=models.CharField(max_lenght=150, blank=True)
    dt_solicitacao=models.CharField(max_lenght=20, verbose_name='Data de solicitação',blank=True)
    dt_conclusao=models.CharField(max_lenght=20, verbose_name='Data de conclusão', blank=True)
    #

class Contribuinte(models.Model):
    telefone=models.CharField(max_lenght=14, verbose_name='Telefone', blank=True)
    cpf=models.CharField(max_lenght=14, verbose_name='CPF')

class Bairro(models.Model):
    nome=models.CharField(max_lenght=150, blank=True)
    
# class *(models.Model):
#     id_OS=models.ForeignKey(OrdemDeServico, verbose_name='')
#     codigo_veiculo=models.CharField(max_lenght=20, verbose_name='Código do veículo', blank=True)


