from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Medico
from .serializers import MedicoSerializer

class MedicoView(View):
  def get(self, request):
    queryset = Doctor.objects.all()
    if request.GET.get('search'):
      queryset = queryset.filter(nome__icontains=request.GET.get('search'))
    if request.GET.getlist('especialidade'):
      for especialidade in request.GET.getlist('especialidade'):
        queryset = queryset.filter(especialidades=especialidade)
    serializer = MedicoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
