from .models import Workday, Workhour
from rest_framework import serializers
from doctors.serializers import DoctorSerializer

class WorkhourSerializer(serializers.ModelSerializer):
  class Meta:
    model = Workhour
    fields = ['hour']

class WorkdaySerializer(serializers.ModelSerializer):
  doctor = DoctorSerializer(many=False)
  hours = WorkhourSerializer(many=True)
  class Meta:
    model = Workday
    fields = ['id', 'date', 'doctor', 'hours']
