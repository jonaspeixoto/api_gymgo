from rest_framework.views import APIView
from ..services import usuario_service
from ..serializers import usuario_serializer
from ..entidades import usuario
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class UsuarioList(APIView):
    def post(self, request, format=None):
        serializer = usuario_serializer.UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["username"]
            senha = serializer.validated_data["password"]
            email = serializer.validated_data["email"]
            cargo = serializer.validated_data["cargo"]
            usuario_novo = usuario.Usuario(nome=nome, senha=senha,email=email,cargo=cargo)
            usuario_bd = usuario_service.cadastrar_usuario(usuario=usuario_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            
        

