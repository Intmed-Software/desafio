from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from specialties.models import Specialty
from specialties.serializers import SpecialtySerializer

class SpecialtyView(View):
    def get(self, request):
        query_filter = request.GET.get('search')
        queryset = Specialty.objects.all()
        if query_filter:
            queryset = queryset.filter(name__contains=query_filter)
        serializer = SpecialtySerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SpecialtySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
