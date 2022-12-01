from django.contrib import admin
from api.models import storage_type

# Register your models here.
@admin.register(storage_type)
class AccessLogAdmin(admin.ModelAdmin):
  list_display = (
            'created_by', 'created_date', 'is_deleted', 'modified_by',
            'modified_date', 'storage_type_id', 'type_name'
        )