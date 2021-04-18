from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Especialidade


class EspecialidadeView(APIView):
  permission_classes = (IsAuthenticated,)
  def get(self, request):    
    query_filter = request.GET.get('search')
    queryset = Especialidade.objects.all()
    if query_filter:
      queryset = queryset.filter(nome__icontains=query_filter)
    return Response({
      'id': q.id,
      'nome': q.nome
    } for q in queryset)
