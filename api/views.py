from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"massage": "Hi there, this is your Django api response!"})