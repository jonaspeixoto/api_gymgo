from ..serializers import planos_serializer
from ..models import Usuario, Perfil, PlanoAssociacao
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def plano_associacao(request):
    print(request.user.cargo)
    if request.user.cargo != 'Gerente':
        return Response({'error': 'Voce não tem permissão para Cadastrar planos de associação'}, status=status.HTTP_403_FORBIDDEN)

    serializer = planos_serializer.PlanosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def listar_planos(request):
    try:
        planos = PlanoAssociacao.objects.all()
        serializer = planos_serializer.PlanosSerializer(planos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def listar_planos_id(request, id):
    
    try:
        plano = PlanoAssociacao.objects.get(id=id)
    except PlanoAssociacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = planos_serializer.PlanosSerializer(plano)
    return Response(serializer.data, status=status.HTTP_200_OK)
