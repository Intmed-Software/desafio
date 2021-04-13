from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorView(View):
    def get(self, request):
        queryset = Doctor.objects.all()
        if request.GET.get('search'):
            queryset = queryset.filter(name__icontains=request.GET.get('search'))
        if request.GET.getlist('especialidade'):
            for specialty in request.GET.getlist('especialidade'):
                queryset = queryset.filter(specialties=specialty)
        serializer = DoctorSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)