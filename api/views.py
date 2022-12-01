from json import JSONDecodeError
from api.serializers import Client_Serializer
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import *
from api.serializers import *



def get_serializer_context(self):
    return {
        'request': self.request,
        'fomat': self.format_kwarg,
        'view': self
    }

def get_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Client_Serializer(*args, **kwargs)

@csrf_exempt
def api_client(request, id=0):
    #using "GET" request


    if request.method == 'GET':
        body = request.body
        data = {}
        try:
            data = json.loads(body)
        except:
            pass
        return JsonResponse(data)


    #using "POST" request
    elif request.method == 'POST':
        try:
            client_data = JSONParser().parse(request)
            client_serializer = Client_Serializer(data=client_data)
            if client_serializer.is_valid(raise_exception=True):
                client_serializer.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to add', safe=False)
        except JSONDecodeError:
            return JsonResponse({'result': 'error', 'message': 'json decoding error'})
    #using "PUT" request
    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client = abc_client.objects.get(abc_client_id = client_data['abc_client_id'])
        client_serializer = Client_Serializer(client, data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to update')
    #using "DELETE" request
    elif request.method == 'DELETE':
        client = abc_client.objects.get(abc_client_id = id)
        client.delete()
        return JsonResponse('Successfully deleted', safe=False)