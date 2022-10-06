from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Bairro(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Bairro')


class Logradouro(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Logradouro')


class Endereco(models.Model):
    referencia = models.CharField(
        max_length=200, verbose_name='Referência', blank=True)
    bairro = models.ForeignKey(
        Bairro, verbose_name='Bairro', on_delete=models.PROTECT)
    logradouro = models.ForeignKey(
        Logradouro, verbose_name='Logradouro', on_delete=models.PROTECT)


# Create your models here.
class Contribuinte(models.Model):
    telefone = models.CharField(
        max_length=14, verbose_name='Telefone', blank=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    nome = models.CharField(max_length=100)


class OrdemDeServico(models.Model):
    numero = models.CharField(max_length=130)
    motivo_reclamacao = models.CharField(max_length=150, blank=True)
    dt_solicitacao = models.CharField(
        max_length=20, verbose_name='Data de solicitação', blank=True)
    dt_conclusao = models.CharField(
        max_length=20, verbose_name='Data de conclusão', blank=True)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT)
    contribuinte = models.ForeignKey(Contribuinte, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=150)
    # VEICULO ???

# class *(models.Model):
#     id_OS=models.ForeignKey(OrdemDeServico, verbose_name='')
#     codigo_veiculo=models.CharField(max_length=20, verbose_name='Código do veículo', blank=True)
#     equipe = models.ManyToManyField(User)
