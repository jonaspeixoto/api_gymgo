from ..services import usuario_service
from ..serializers import usuario_serializer
from ..models import Usuario, Perfil
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def cadastro (request):
    """
    Realiza o cadastro de um novo usuário.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna um token de autenticação e os dados do usuário cadastrado.

    """
    serializer = usuario_serializer.UsuarioSerializer(data=request.data) 

    if serializer.is_valid():
        serializer.save()
        user = Usuario.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user":serializer.data},status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login (request):
    """
    Realiza o login de um usuário existente.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna um token de autenticação e os dados do usuário logado.
    
    """
    username = request.data['username']
    password = request.data['password']
    user = get_object_or_404(Usuario, username=username)

    if not user.check_password(password):
        return Response({"detalhe": "Credenciais invalidas"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, create = Token.objects.get_or_create(user=user)
    serializer = usuario_serializer.UsuarioSerializer(instance=user)
    return Response({"token": token.key, "user":serializer.data},status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout (request):
    """
    Realiza o logout do usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna uma mensagem indicando que o logout foi bem sucedido.
    """

    request.auth.delete()
    return Response({"detalhes": "Logout bem sucedido"}, status=status.HTTP_200_OK )

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil_cadastro(request):
    """
    Realiza o cadastro do perfil de um usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna os dados do perfil cadastrado.
    """
    dados_perfil = {'usuario': request.user.id, **request.data}
    serializer = usuario_serializer.PerfilUsuarioSerializer(data=dados_perfil)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'detail': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):
    """
    Realiza o cadastro do perfil de um usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna os dados do perfil cadastrado.
    """
    usuario = Usuario.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(id=request.user.id)
    serializer_usuario = usuario_serializer.UsuarioSerializer(usuario)
    serializer_perfil_usuario = usuario_serializer.PerfilUsuarioSerializer(perfil_usuario)
    return Response({"Usuario":serializer_usuario.data,"perfil":serializer_perfil_usuario.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def fazer_checkin(request):
    """
    Realiza o check-in do aluno associado ao usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.

    Returns:
    - Response: Retorna os dados do check-in realizado.
    """
    dados_checkin = {'aluno': request.user.id}
    serializer = usuario_serializer.CheckInUsuarioSerializer(data=dados_checkin)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'detail': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    """
    Testa a autenticação e retorna uma mensagem indicando que o usuário está autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição GET.

    Returns:
    - Response: Retorna uma mensagem indicando que o usuário está autenticado.
    """
    return Response(f'usuario autenticado {request.user.email}')

