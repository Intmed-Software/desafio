from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Especialidade
from .serializers import EspecialidadeSerializer

class EspecialidadeView(View):
  def get(self, request):
    query_filter = request.GET.get('search')
    queryset = Especialidade.objects.all()
    if query_filter:
      queryset = queryset.filter(nome__icontains=query_filter)
    serializer = EspecialidadeSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
