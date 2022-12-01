from json import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import F
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
    return self.StorageType_Serializer(*args, **kwargs)

@csrf_exempt
def api_client(request, pk):
    access_id = storage_type.objects.get(pk=pk)
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
            client_serializer = StorageType_Serializer(data=client_data)
            if client_serializer.is_valid(raise_exception=True):
                client_serializer.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to add', safe=False)
        except JSONDecodeError:
            return JsonResponse({'result': 'error', 'message': 'json decoding error'})

    #using "PUT" request
    elif request.method == 'PUT':
        try:
            client_data = JSONParser().parse(request)
            logs = Access_Serializer(access_id, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        storage_type.objects.filter(storage_type_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)