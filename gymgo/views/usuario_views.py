
from ..services import usuario_service
from ..serializers import usuario_serializer
from ..models import Usuario
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login (request):
    user = get_object_or_404(Usuario, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
    token, create = Token.objects.get_or_create(user=user)
    serializer = usuario_serializer.UsuarioSerializer(instance=user)
    return Response({"token": token.key, "user":serializer.data},status=status.HTTP_201_CREATED)
            
        
@api_view(['POST'])
def cadastro (request):
    serializer = usuario_serializer.UsuarioSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        user = Usuario.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        print("teste")
        return Response({"token": token.key, "user":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f'usuario autenticado {request.user.email}')

