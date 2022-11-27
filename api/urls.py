from django.urls import path, re_path
from api import views

urlpatterns = [
    path('abc_client/', views.api_client)
]