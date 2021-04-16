from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Dia, Horario
from medicos.models import Medico
from .serializers import DiaSerializer
from datetime import datetime

class AgendaView(APIView):
  permission_classes = (IsAuthenticated,)
  def get(self, request):
    medicos_ids = []
    if request.GET.getlist('medico'):
      for medico in request.GET.getlist('medico'):
        medicos_ids.append(int(medico))
    if request.GET.getlist('especialidade'):
      for especialidade in request.GET.getlist('especialidade'):
        medicos_ids += Medico.objects.filter(especialidades=especialidade).values_list('id', flat=True)
    queryset = Dia.objects.filter(data__gte=datetime.now().date()).order_by('data')
    if medicos_ids:
      queryset = queryset.filter(medico_id__in=medicos_ids)

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
      'horarios': [h.hora for h in Horario.objects.filter(dia_id=q.id)],
    } for q in queryset)
