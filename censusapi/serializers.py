from rest_framework import serializers
from .models import State
from .models import District

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

# class DistrictSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = District
#         fields = '__all__'  # This will include all fields from the District model

# class StateDetailSerializer(serializers.ModelSerializer):
#     districts = DistrictSerializer(many=True)  # Nested serializer for districts

#     class Meta:
#         model = State
#         fields = ['id', 'name', 'abbreviation', 'districts']  # Include overall state info