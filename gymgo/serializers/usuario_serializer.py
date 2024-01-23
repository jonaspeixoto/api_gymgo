from rest_framework import serializers
from ..models import Usuario, Perfil, CheckIn


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Usuario
        fields = ('id','username','cargo','email','password','cpf','telefone')


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Perfil
        fields = '__all__'

class CheckInUsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CheckIn
        fields = '__all__'

    
   