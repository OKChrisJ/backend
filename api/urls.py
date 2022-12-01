from django.urls import path, re_path
from api import views

urlpatterns = [
    re_path(r'^abc_client$', views.api_client, name='api_client'),
    re_path(r'^abc_client/([0-9]+)$', views.api_client, name='api_client'),
    re_path(r'^$', views.api_client, name='api_client')
]