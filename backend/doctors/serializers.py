from .models import Doctor
from rest_framework import serializers
from specialties.serializers import SpecialtySerializer


class DoctorSerializer(serializers.ModelSerializer):

  specialties = SpecialtySerializer(many=True)

  class Meta:
    model = Doctor
    fields = ['id', 'name', 'crm', 'email', 'phone', 'specialties']
