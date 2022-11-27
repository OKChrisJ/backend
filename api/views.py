from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import *
from api.serializers import *

@csrf_exempt
def api_client(request, id=0):
    if request.method == 'GET':
        client = abc_client.objects.all()
        client_serializer = Client_Serializer(client, many=True)
        return JsonResponse(client_serializer.data, safe=False)
    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = Client_Serializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonReponse('Added Successfully', safe=False)
        return JSonReponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client = abc_client.objects.get(abc_client_id = client_data['abc_client_id'])
        client_serializer = Client_Serializer(client, data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonReponse('Added Successfully', safe=False)
        return JSonReponse('Failed to update')
    elif request.method == 'DELETE':
        client = abc_client.objects.get(abc_client_id = id)
        client.delete()
        return JsonResponse('Successfully deleted', safe=False)