from .models import Specialty
from rest_framework import serializers


class SpecialtySerializer(serializers.ModelSerializer):
  class Meta:
    model = Specialty
    fields = ['id', 'name']