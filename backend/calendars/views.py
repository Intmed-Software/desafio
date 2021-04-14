from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Workday, Workhour
from doctors.models import Doctor
from .serializers import WorkdaySerializer
from datetime import datetime

class CalendarView(View):
  def get(self, request):
    doctors_ids = []
    if request.GET.getlist('medico'):
      for doctor in request.GET.getlist('medico'):
        doctors_ids.append(int(doctor))
    if request.GET.getlist('especialidade'):
      for specialty in request.GET.getlist('especialidade'):
        doctors_ids += Doctor.objects.filter(specialties=specialty).values_list('id', flat=True)
    queryset = Workday.objects.filter(date__gte=datetime.now().date()).order_by('date')
    if doctors_ids:
      queryset = queryset.filter(doctor__in=doctors_ids)
    serializer = WorkdaySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
