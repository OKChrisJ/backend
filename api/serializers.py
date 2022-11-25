from rest_framework import serializers
from api.models import *

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = abc_client
        fields = (
            'abc_client_id', 'client_name', 'company_address_id'
            'created_by', 'created_date', 'is_deleted', 'modified_by',
            'modified_date', 'phone_number'
            )

class Resource_Serializer(serializers.ModelSerializer):
    class Meta:
        model = abc_resource
        fields = (
            'abc_resource_id', 'created_by', 'created_date',
            'current_number_of_resources', 'inventory_id', 'is_deleted',
            'max_number_of_resources', 'modified_by', 'modified_date',
            'resource_name', 'resource_type_id'
        )

class Access_Serializer(serializers.ModelSerializer):
    class Meta:
        model = access_log
        fields = (
            'access_log_id', 'action', 'field_name', 'screen_name',
            'table_name', 'username'
        )

class Address_Serializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = (
            'address_id', 'address_line_1', 'address_line_2', 'city',
            'country', 'created_by', 'created_date', 'is_deleted',
            'modified_by', 'modified_date', 'postal_code', 'state'
        )

class ClientContact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = client_contacts
        fields = (
            'abc_client_id', 'client_contacts_id', 'contact_id',
            'created_by', 'created_date', 'is_deleted', 'modified_by',
            'modified_date'
        )

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = (
            'contact_id', 'created_by', 'created_date', 'email_address',
            'first_name', 'middle_name', 'last_name', 'is_deleted',
            'modified_by', 'modified_date', 'phone_number'
        )

class Inventory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = (
            'abc_client_id', 'address_id', 'created_by', 'created_date',
            'inventory_id', 'inventory_name', 'is_deleted',
            'max_item_capacity', 'modified_by', 'modified_date',
            'storage_type_id'
        )

class ResourceType_Serializer(serializers.ModelSerializer):
    class Meta:
        model = resource_type
        fields = (
            'created_by', 'created_date', 'is_deleted', 'modified_by',
            'modified_date', 'resource_type_id', 'type_name'
        )

class StorageType_Serializer(serializers.ModelSerializer):
    class Meta:
        model = storage_type
        fields = (
            'created_by', 'created_date', 'is_deleted', 'modified_by',
            'modified_date', 'storage_type_id', 'type_name'
        )