from ..models import Usuario
from django.http import Http404

def cadastrar_usuario(usuario):
    return Usuario.objects.create(username=usuario.nome, password=usuario.senha, email=usuario.email, cargo=usuario.cargo)
