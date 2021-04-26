from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Consulta
from agendas.models import Disponibilidade, Horario
from datetime import datetime
import json


class ConsultaList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        print("Pegando as Consultas do usuário!!!")
        print(request.user.id)
        now = datetime.now()
        queryset = Consulta.objects.filter(usuario=request.user.id).filter(Q(disponibilidade__data__gte=now.date()) or Q(horario__hora__gte=now.time())).order_by('disponibilidade__data', 'horario__hora')
        return Response({
            'id': consulta.id,
            'dia': consulta.disponibilidade.data,
            'horario': consulta.horario.hora,
            'data_agendamento': consulta.data_agendamento,
            'medico': consulta.disponibilidade.medico.nome,
            'especialidade': consulta.disponibilidade.medico.especialidade.nome
        } for consulta in queryset)

    def post(self, request):
        permission_classes = (IsAuthenticated,)
        disponibilidade = Disponibilidade.objects.get(id=request.data['agenda_id'])
        horario = Horario.objects.filter(disponibilidade=request.data['agenda_id'], hora=request.data['horario']).first()
        consulta = Consulta()
        consulta.usuario = request.user
        consulta.disponibilidade = disponibilidade
        consulta.horario = horario
        consulta.save()
        return Response({
            "id": consulta.id,
            "dia": disponibilidade.data,
            "horario": consulta.horario.hora,
            "data_agendamento": consulta.data_agendamento,
            "medico": {
                "id": disponibilidade.medico.id,
                "crm": disponibilidade.medico.crm,
                "nome": disponibilidade.medico.nome,
                'especialidade': {
                    'id': disponibilidade.medico.especialidade.id, 
                    'name': disponibilidade.medico.especialidade.nome
                }
            }
        })

class ConsultaDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, id=None, format=None):
        consulta = Consulta.objects.get(id=id)
        consulta.delete()
        return Response({})