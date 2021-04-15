from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Dia
from medicos.models import Medico
from .serializers import DiaSerializer
from datetime import datetime

class AgendaView(View):
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
    serializer = DiaSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
