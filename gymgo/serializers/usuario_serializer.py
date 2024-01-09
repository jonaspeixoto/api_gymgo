from rest_framework import serializers
from ..models import Usuario, Perfil


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Usuario
        fields = ('id','username','cargo','email','password','cpf','telefone')


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Perfil
        fields = ('idade', 'peso', 'altura','cep', 'numero','usuario')


    
   