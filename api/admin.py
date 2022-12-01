from django.contrib import admin
from api.models import *

# Register your models here.
@admin.register(address)
class AddressAdmin(admin.ModelAdmin):
  list_display = (
    'address_id', 'address_line_1', 'address_line_2', 'city',
    'country', 'created_by', 'created_date', 'is_deleted',
    'modified_by', 'modified_date', 'postal_code', 'state'
  )

@admin.register(storage_type)
class StorageTypeAdmin(admin.ModelAdmin):
  list_display = (
    'created_by', 'created_date', 'is_deleted', 'modified_by',
    'modified_date', 'storage_type_id', 'type_name'
  )

@admin.register(resource_type)
class ResourceTypeAdmin(admin.ModelAdmin):
  list_display = (
    'created_by', 'created_date', 'is_deleted', 'modified_by',
    'modified_date', 'resource_type_id', 'type_name'
  )

@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = (
    'contact_id', 'created_by', 'created_date', 'email_address',
    'first_name', 'middle_name', 'last_name', 'is_deleted',
    'modified_by', 'modified_date', 'phone_number'
  )

@admin.register(abc_client)
class AbcClientAdmin(admin.ModelAdmin):
  list_display = (
    'abc_client_id', 'client_name', 'company_address_id',
    'created_by', 'created_date', 'is_deleted', 'modified_by',
    'modified_date', 'phone_number'
  )

@admin.register(inventory)
class InventoryAdmin(admin.ModelAdmin):
  list_display = (
    'abc_client_id', 'address_id', 'created_by', 'created_date',
    'inventory_id', 'inventory_name', 'is_deleted',
    'max_item_capacity', 'modified_by', 'modified_date',
    'storage_type_id'
  )

@admin.register(abc_resource)
class ResourceAdmin(admin.ModelAdmin):
  list_display = (
    'abc_resource_id', 'created_by', 'created_date',
    'current_number_of_resources', 'inventory_id', 'is_deleted',
    'max_number_of_resources', 'modified_by', 'modified_date',
    'resource_name', 'resource_type_id'
  )

@admin.register(client_contacts)
class ClientContactAdmin(admin.ModelAdmin):
  list_display = (
    'abc_client_id', 'client_contacts_id', 'contact_id',
    'created_by', 'created_date', 'is_deleted', 'modified_by',
    'modified_date'
  )

@admin.register(access_log)
class AccessLogAdmin(admin.ModelAdmin):
  list_display = (
    'access_log_id', 'action', 'field_name', 'screen_name',
    'table_name', 'username'
  )