from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .serializers import StateSerializer
from .models import State, District
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Fetching Bureau of Transportation Statistics API
import requests
# Create your views here.

# #         self.base_url = 'https://data.ojp.usdoj.gov/resource/imsf-b5s7.geojson?statefp=${}&cd116fp=${}'
# @api_view(['GET'])
# def find_district(request):
#     district = None
#     if request.method == "POST":
#         form = DistrictForm(request.POST)
#         if form.is_valid():
#             state = form.cleaned_data['state']
#             district_number = form.cleaned_data['district_number']
#             # Redirect to the district details view
#             return redirect('district_details', state_abbreviation=state.abbreviation, district_number=district_number)
#     else:
#         form = DistrictForm()
    
#     return render(request, 'app/find_district.html', {'form': form, 'district': district})


#todo: try, else get from census api
@api_view(['GET', 'POST'])
def state_list(request, format=None):

    #get all the drinks
    #serialize
    #return json
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def state_detail(request, state_id, format=None):

    try: 
        state = State.objects.get(id=state_id)
    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        #will implement census.api call here
    
    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


