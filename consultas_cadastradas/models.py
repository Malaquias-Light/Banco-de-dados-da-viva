from django.conf.locale import de
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome completo')
    data_de_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    genero = models.CharField(max_length=10, verbose_name='Gênero')
    convenio_medico = models.CharField(max_length=100, verbose_name='Convênio médico')
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Paciente'

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome completo')
    especialidade = models.TextField(null=True, blank=True, verbose_name='Especialidade')
    crm = models.CharField(max_length=20, verbose_name='CRM')
    data_de_nascimento = models.DateField(verbose_name='Data de nascimento')
    localização = models.TextField(null=True, blank=True, verbose_name='Localização')
    preco_consulta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço da consulta')
    classificacao_pacientes = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Classificação pelos pacientes')
    genero = models.CharField(max_length=10, verbose_name='Gênero')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Médico'

    def __str__(self):
        return self.nome
