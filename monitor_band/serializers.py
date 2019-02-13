from rest_framework import serializers
from .models import TempValues


class TempValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempValues
        fields = "__all__"
