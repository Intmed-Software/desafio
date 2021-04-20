from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Medico
from especialidades.models import Especialidade
from rest_framework.permissions import IsAuthenticated

class MedicoView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = Medico.objects.all()
        if request.GET.get('search'):
            queryset = queryset.filter(nome__icontains=request.GET.get('search'))
        if request.GET.getlist('especialidade'):
            for especialidade in request.GET.getlist('especialidade'):
                queryset = queryset.filter(especialidades=especialidade)

        return Response({
            'id': q.id,
            'nome': q.nome,
            'crm': q.crm,
            'especialidade': [{
                'id': e.id, 
                'name': e.nome
            } for e in q.especialidades.all()]
        } for q in queryset)
