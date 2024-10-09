from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StateSerializer
from .models import State

# Create your views here.
def state_list(request):

    #get all the drinks
    #serialize
    #return json

    states = State.objects.all()
    states_serializer = StateSerializer(states, many=True)
    return JsonResponse({"states":states_serializer.data}, safe=False)

    # return render(request, 'censusapi/state_list.html', {})