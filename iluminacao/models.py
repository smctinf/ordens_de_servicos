from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from almoxarifado.models import Material
from autenticacao.models import Pessoa

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

class Funcionario_OS(models.Model):
    def __str__(self):
        return self.pessoa.nome
    NIVEL_CHOICES=(
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )

    pessoa = models.ForeignKey(Pessoa, models.CASCADE)
    tipo_os =  models.ManyToManyField(Tipo_OS)
    nivel = models.CharField(max_length=1, verbose_name='Nível de acesso', choices=NIVEL_CHOICES, null=True, default='0')
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class OrdemDeServico(models.Model):
    STATUS_CHOICES=(
        ('0','Novo'),
        ('1','Aguardando'),
        ('2','Execução'),
    )
    PRIORIDADE_CHOICES=(
        ('0','N/D'),
        ('1','Normal'),
        ('2','Urgente'),
    )

    
    tipo=models.ForeignKey(Tipo_OS, on_delete=models.PROTECT, null=True)
    numero = models.CharField(max_length=130, verbose_name='Nº da OS')
    prioridade =models.CharField(max_length=1, verbose_name='Prioridade', default='0', choices=PRIORIDADE_CHOICES, null=True)

    dt_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de solicitação', blank=True)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    referencia = models.CharField(max_length=200, verbose_name='Referência', blank=True)

    contribuinte = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)   

    motivo_reclamacao = models.TextField(verbose_name='Motivo da reclamação')            
    
    status =models.CharField(max_length=1, verbose_name='Status', choices=STATUS_CHOICES, null=True, default='0')

    dt_conclusao = models.DateTimeField(verbose_name='Data de conclusão', blank=True, null=True)

    def gerar_protocolo(self):
        return 'ok'
        
class OS_ext(models.Model):    
    os=models.ForeignKey(OrdemDeServico, on_delete=models.PROTECT)
    equipe=models.ManyToManyField(Funcionario_OS, blank=True, null=True)
    cod_veiculo=models.CharField(max_length=14, verbose_name='Código do veículo', blank=True)

class OS_Linha_Tempo(models.Model):
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    

class MateriaisUsados(models.Model):
    os=models.ForeignKey(OrdemDeServico, on_delete=models.PROTECT)
    material=models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade=models.IntegerField()