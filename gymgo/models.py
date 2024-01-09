from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class Usuario(AbstractUser):
    CHOICHE_CARGO = (('Aluno', 'Aluno'),
                     ('Gerente', 'Gerente'),
                     ('Funcionario', 'Funcionario')
                     )
    cargo = models.CharField(max_length=20,choices = CHOICHE_CARGO)
    cpf =  models.CharField(max_length=20, null= True)
    telefone = models.CharField(max_length=20, null=True)
    

class Perfil(models.Model):
    # foto_perfil = models.ImageField()
    idade = models.IntegerField(null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
    altura = models.DecimalField(max_digits=5, decimal_places=2, help_text="Altura em metros")
    cep = models.IntegerField(null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, unique=True)

