from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Disponibilidade
from medicos.models import Medico
from datetime import datetime

class AgendaView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = Disponibilidade.objects.filter(data__gte=datetime.now().date()).order_by('data')
        queryset = self.filtro_medicos(queryset, request.GET.get('medico'), request.GET.get('especialidade'))

        if request.GET.get('data_inicio') and request.GET.get('data_final'):
            queryset = queryset.filter(data__range=(request.GET.get('data_inicio'), request.GET.get('data_final')))

        horarios_exclude_id = self.horarios_ocupados(queryset)

        return Response({
            'id': q.id,
            'dia': q.data,
            'medico': {
                'id': q.medico.id,
                'nome': q.medico.nome,
                'crm': q.medico.crm,
                'especialidade': [{
                    'id': e.id, 
                    'name': e.nome
                } for e in q.medico.especialidades.all()]
            },
            # 'horarios': [h.hora for h in q.horario_set.exclude(id__in=horarios_exclude_id)],
            'horarios': self.lista_horarios_vagos(q.horario_set.all()),
        } for q in queryset)

    def filtro_medicos(self, queryset=None, medicos=None, especialidades=None):
        medicos_ids = []
        if medicos:
            for medico in medicos.split(","):
                medicos_ids.append(int(medico))
        if especialidades:
            for especialidade in especialidades.split(","):
                medicos_ids += Medico.objects.filter(especialidades=especialidade).values_list('id', flat=True)
        if medicos_ids:
            medicos_ids = list(dict.fromkeys(medicos_ids))
            queryset = queryset.filter(medico_id__in=medicos_ids)
        return queryset

    def horarios_ocupados(self, queryset=None):
        # Faz uma lista de IDs de Horários 
        # que já possuem uma consulta marcada
        horarios_id = []
        for disponibilidade in queryset:
            for horario in disponibilidade.horario_set.all():
                consulta = horario.consulta_set.first()
                if consulta:
                    horarios_id.append(int(horario.id))
        return horarios_id

    def lista_horarios_vagos(self, queryset=None):
        horarios_list = []
        for horario in queryset:
            if not horario.consulta_set.first():
                horarios_list.append(horario.hora)
        return horarios_list
