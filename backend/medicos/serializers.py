from rest_framework import serializers
from .models import Medico
from especialidades.serializers import EspecialidadeSerializer

class MedicoSerializer(serializers.ModelSerializer):
  especialidades = EspecialidadeSerializer(many=True)
  class Meta:
    model = Medico
    fields = ['id', 'nome', 'crm', 'email', 'telefone', 'especialidades']