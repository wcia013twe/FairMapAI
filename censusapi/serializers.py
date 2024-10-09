from rest_framework import serializers
from .models import State
from .models import District

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'