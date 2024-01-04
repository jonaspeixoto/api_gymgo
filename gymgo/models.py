from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    CHOICHE_CARGO = (('A', 'aluno'),
                     ('G', 'Gerente'),
                     ('F', 'funcionario')
                     )
    cargo = models.CharField(max_length=1,choices = CHOICHE_CARGO)
    




# Create your models here.
