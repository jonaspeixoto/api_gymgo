from ..services import usuario_service
from ..serializers import usuario_serializer
from ..models import Usuario, Perfil
from .planos_views import PlanoAssociacao
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
        return Response({"detail": "Credenciais invalidas"}, status=status.HTTP_400_BAD_REQUEST)
    
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
    return Response({"detail": "Logout bem sucedido"}, status=status.HTTP_200_OK )

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
    Realiz consulta dos dados do perfil de um usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição GET.

    Returns:
    - Response: Retorna os dados do perfil cadastrado.
    """
    usuario = Usuario.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(usuario=request.user.id)
    serializer_usuario = usuario_serializer.UsuarioSerializer(usuario)
    serializer_perfil_usuario = usuario_serializer.PerfilUsuarioSerializer(perfil_usuario)
    return Response({"Usuario":serializer_usuario.data,"perfil":serializer_perfil_usuario.data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editar_perfil(request):
    """
    Edita o perfil de um usuário autenticado.

    Parameters:
    - request: Objeto contendo os dados da requisição PUT.

    Returns:
    - Response: Retorna os dados do perfil editado.

    """
    try:
        usuario = Usuario.objects.get(id=request.user.id)
        perfil_usuario = Perfil.objects.get(usuario=request.user.id)
    except Usuario.DoesNotExist:
        return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Perfil.DoesNotExist:
        return Response({"detail": "Perfil não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    serializer_usuario = usuario_serializer.UsuarioSerializer(usuario, data=request.data.get('Usuario'))
    if serializer_usuario.is_valid():
        serializer_usuario.save()
    else:
        return Response({"errors": serializer_perfil_usuario.errors}, status=status.HTTP_400_BAD_REQUEST)

    serializer_perfil_usuario = usuario_serializer.PerfilUsuarioSerializer(perfil_usuario, data=request.data.get('perfil'))
    if serializer_perfil_usuario.is_valid():
        serializer_perfil_usuario.save()
    else:
        return Response({"errors": serializer_usuario.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"Usuario": serializer_usuario.data, "perfil": serializer_perfil_usuario.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def cadastrar_aluno_plano(request,id):
    """
    Realiza o cadastro em um plano de associaçao.

    Parameters:
    - request: Objeto contendo os dados da requisição POST.
    - id: Id conrrespondente ao plano de associação.

    Returns:
    - Response: Retorna o id do usuario e o id do plano que o mesmo foi associado.
    """
    try:
        usuario = Usuario.objects.get(id=request.user.id)
    except Usuario.DoesNotExist:
        return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
         plano =PlanoAssociacao.objects.get(id=id)
    except Usuario.DoesNotExist:
        return Response({"detail": "Plano não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    usuario.plano = plano
    usuario.save()
    return Response({"Usuario": usuario.id, "Plano": plano.id})


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

