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


#Access Logs

def get_access_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Access_Serializer(*args, **kwargs)

@csrf_exempt
def access_log_db(request, pk):
    access_id = access_log.objects.get(pk=pk)
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
            client_serializer = Access_Serializer(data=client_data)
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


#Address

def get_address_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Address_Serializer(*args, **kwargs)

@csrf_exempt
def address_db(request, pk):
    the_address = address.objects.get(pk=pk)
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
            client_serializer = Address_Serializer(data=client_data)
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
            logs = Address_Serializer(the_address, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        address.objects.filter(address_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)


#Storage_type

def get_storage_type_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.StorageType_Serializer(*args, **kwargs)

@csrf_exempt
def storage_type_db(request, pk):
    the_storage_type = storage_type.objects.get(pk=pk)
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
            logs = StorageType_Serializer(the_storage_type, data = client_data)
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


#Resource_type

def get_resource_type_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.ResourceType_Serializer(*args, **kwargs)

@csrf_exempt
def resource_type_db(request, pk):
    the_resource_type = resource_type.objects.get(pk=pk)
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
            client_serializer = ResourceType_Serializer(data=client_data)
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
            logs = ResourceType_Serializer(the_resource_type, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        resource_type.objects.filter(resource_type_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)


#Contact

def get_contact_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Contact_Serializer(*args, **kwargs)

@csrf_exempt
def contact_db(request, pk):
    the_contact = contact.objects.get(pk=pk)
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
            client_serializer = Contact_Serializer(data=client_data)
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
            logs = Contact_Serializer(the_contact, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        contact.objects.filter(contact_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)

#abc_client

def get_client_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Client_Serializer(*args, **kwargs)

@csrf_exempt
def abc_client_db(request, pk):
    the_client= abc_client.objects.get(pk=pk)
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
        try:
            client_data = JSONParser().parse(request)
            logs = Client_Serializer(the_client, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        abc_client.objects.filter(abc_client_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)

#inventory

def get_inventory_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Inventory_Serializer(*args, **kwargs)

@csrf_exempt
def inventory_db(request, pk):
    the_inventory= inventory.objects.get(pk=pk)
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
            client_serializer = Inventory_Serializer(data=client_data)
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
            logs = Inventory_Serializer(the_inventory, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        inventory.objects.filter(inventory_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)

#abc_resource

def get_abc_resource_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.Resource_Serializer(*args, **kwargs)

@csrf_exempt
def abc_resource_db(request, pk):
    the_resources= resource.objects.get(pk=pk)
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
            client_serializer = Resource_Serializer(data=client_data)
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
            logs = Resource_Serializer(the_resources, data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        resource.objects.filter(abc_resource_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)

#abc_resource

def get_client_contact_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.ClientContact_Serializer(*args, **kwargs)

@csrf_exempt
def client_contacts_db(request, pk):
    the_client_contacts = client_contacts.objects.get(pk=pk)
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
            client_serializer = ClientContact_Serializer(data=client_data)
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
            logs = ClientContact_Serializer(the_client_contacts , data = client_data)
            if logs.is_valid():
                logs.save()
                return JsonResponse('Added Successfully', safe=False)
            return JsonResponse('Failed to update')
        except JSONDecodeError:
            return JsonResponse('Failed to decode')

    #using "DELETE" request
    elif request.method == 'DELETE':
        client_contacts.objects.filter(client_contacts_id=pk).update(
            is_deleted = F('is_deleted') + 1
        )
        return JsonResponse('Successfully deleted', safe=False)

