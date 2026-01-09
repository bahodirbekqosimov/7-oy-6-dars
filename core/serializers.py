from rest_framework import serializers
from .models import YourModel

class SerializerName(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = []
