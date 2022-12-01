from django.urls import path, re_path
from api import views

urlpatterns = [
    #access log paths
    re_path(r'^access_log$', views.access_log_db, name='access_log'),
    re_path(r'^access_log/([0-9]+)$', views.access_log_db, name='access_log'),
    re_path(r'^access_log/(?P<pk>[0-9]+)$', views.access_log_db, name='access_log'),

    #address paths
    re_path(r'^address$', views.address_db, name='address'),
    re_path(r'^address/([0-9]+)$', views.address_db, name='address'),
    re_path(r'^address/(?P<pk>[0-9]+)$', views.address_db, name='address'),

    #storage_type paths
    re_path(r'^storage_type$', views.storage_type_db, name='storage_type'),
    re_path(r'^storage_type/([0-9]+)$', views.storage_type_db, name='storage_type'),
    re_path(r'^storage_type/(?P<pk>[0-9]+)$', views.storage_type_db, name='storage_type'),

    #resource_type paths
    re_path(r'^resource_type$', views.resource_type_db, name='resource_type'),
    re_path(r'^resource_type/([0-9]+)$', views.resource_type_db, name='resource_type'),
    re_path(r'^resource_type/(?P<pk>[0-9]+)$', views.resource_type_db, name='resource_type'),

    #contact paths
    re_path(r'^contact$', views.contact_db, name='contact'),
    re_path(r'^contact/([0-9]+)$', views.contact_db, name='contact'),
    re_path(r'^contact/(?P<pk>[0-9]+)$', views.contact_db, name='contact'),

    #abc_client paths
    re_path(r'^abc_client$', views.abc_client_db, name='abc_client'),
    re_path(r'^abc_client/([0-9]+)$', views.abc_client_db, name='abc_client'),
    re_path(r'^abc_client/(?P<pk>[0-9]+)$', views.abc_client_db, name='abc_client'),

    #inventory paths
    re_path(r'^inventory$', views.inventory_db, name='inventory'),
    re_path(r'^inventory/([0-9]+)$', views.inventory_db, name='inventory'),
    re_path(r'^inventory/(?P<pk>[0-9]+)$', views.inventory_db, name='inventory'),

    #abc_resource paths
    re_path(r'^abc_resource$', views.abc_resource_db, name='abc_resource'),
    re_path(r'^abc_resource/([0-9]+)$', views.abc_resource_db, name='abc_resource'),
    re_path(r'^abc_resource/(?P<pk>[0-9]+)$', views.abc_resource_db, name='abc_resource'),

    #client_contacts paths
    re_path(r'^client_contacts$', views.client_contacts_db, name='client_contacts'),
    re_path(r'^client_contacts/([0-9]+)$', views.client_contacts_db, name='client_contacts'),
    re_path(r'^client_contacts/(?P<pk>[0-9]+)$', views.client_contacts_db, name='client_contacts'),
]