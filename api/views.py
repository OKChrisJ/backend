from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import *
from api.serializers import *

def api_home(request, *args, **kwargs):
    return JsonResponse({"massage": "Hi there, this is your Django api response!"})