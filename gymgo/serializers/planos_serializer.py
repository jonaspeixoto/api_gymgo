from rest_framework import serializers
from ..models import PlanoAssociacao


class PlanosSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = PlanoAssociacao
        fields = '__all__'


    
   