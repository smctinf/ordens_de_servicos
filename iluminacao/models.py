from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from almoxarifado.models import Material

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

class Tipo_OS(models.Model):
    
    nome=models.CharField(max_length=100, verbose_name='Tipo de OS', blank=True)
    sigla=models.CharField(max_length=10, verbose_name='Sigla', blank=True, null=True)
    def __str__(self):
        return self.nome

class Contribuinte(models.Model):
    telefone = models.CharField(max_length=14, verbose_name='Telefone', blank=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    nome = models.CharField(max_length=100)

class Funcionario(models.Model):

    def __str__(self):
        return self.nome

    telefone = models.CharField(max_length=14, verbose_name='Telefone', blank=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    nome = models.CharField(max_length=100, verbose_name='Nome do funcionário')

class OrdemDeServico(models.Model):
    STATUS_CHOICES=(
        ('0','Novo'),
        ('1','Aguardando'),
        ('2','Execução'),
    )
    PRIORIDADE_CHOICES=(
        ('0','Normal'),
        ('1','Urgente'),
    )

    
    tipo=models.ForeignKey(Tipo_OS, on_delete=models.PROTECT, null=True)
    numero = models.CharField(max_length=130, verbose_name='Nº da OS')
    prioridade =models.CharField(max_length=1, verbose_name='Prioridae', choices=PRIORIDADE_CHOICES, null=True)

    dt_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de solicitação', blank=True)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    referencia = models.CharField(max_length=200, verbose_name='Referência', blank=True)

    nome = models.CharField(max_length=100, verbose_name='Nome do contribuinte')
    cpf = models.CharField(max_length=14, verbose_name='CPF do contribuinte')
    telefone = models.CharField(max_length=14, verbose_name='Telefone do contribuinte', blank=True)    

    motivo_reclamacao = models.TextField(verbose_name='Motivo da reclamação')            
    
    status =models.CharField(max_length=1, verbose_name='Status', choices=STATUS_CHOICES, null=True)

    dt_conclusao = models.DateTimeField(verbose_name='Data de conclusão', blank=True, null=True)

class OS_ext(models.Model):    
    os=models.ForeignKey(OrdemDeServico, on_delete=models.PROTECT)
    equipe=models.ManyToManyField(Funcionario, blank=True, null=True)
    cod_veiculo=models.CharField(max_length=14, verbose_name='Código do veículo', blank=True)

class MateriaisUsados(models.Model):
    os=models.ForeignKey(OrdemDeServico, on_delete=models.PROTECT)
    material=models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade=models.IntegerField()