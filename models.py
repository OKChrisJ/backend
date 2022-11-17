# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbcClient(models.Model):
    abc_client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    company_address = models.ForeignKey('Address', models.DO_NOTHING, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc_client'


class AbcResource(models.Model):
    abc_resource_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey('Inventory', models.DO_NOTHING)
    resource_type = models.ForeignKey('ResourceType', models.DO_NOTHING)
    resource_name = models.CharField(max_length=45)
    max_number_of_resources = models.BigIntegerField()
    current_number_of_resources = models.BigIntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc_resource'


class AccessLog(models.Model):
    access_log_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=45)
    action = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    field_name = models.CharField(max_length=45, blank=True, null=True)
    screen_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_log'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)
    city = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address'


class ApiAbcClient(models.Model):
    id = models.BigAutoField(primary_key=True)
    abc_client_id = models.IntegerField()
    client_name = models.CharField(max_length=100)
    company_address_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    phone_number = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'api_abc_client'


class ApiAbcResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    abc_resource_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    current_number_of_resources = models.IntegerField()
    inventory_id = models.IntegerField()
    is_deleted = models.IntegerField()
    max_number_of_resources = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    resource_name = models.CharField(max_length=45)
    resource_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_abc_resource'


class ApiAccessLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_log_id = models.IntegerField()
    action = models.CharField(max_length=45)
    field_name = models.CharField(max_length=45)
    screen_name = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'api_access_log'


class ApiAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    postal_code = models.CharField(max_length=45)
    state = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'api_address'


class ApiClientContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    abc_client_id = models.IntegerField()
    client_contacts_id = models.IntegerField()
    contact_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'api_client_contacts'


class ApiContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    email_address = models.CharField(max_length=254)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=50)
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'api_contact'


class ApiInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    abc_client_id = models.IntegerField()
    address_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    inventory_id = models.IntegerField()
    inventory_name = models.CharField(max_length=45)
    is_deleted = models.IntegerField()
    max_item_capacity = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    storage_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_inventory'


class ApiResourceType(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    resource_type_id = models.IntegerField()
    type_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'api_resource_type'


class ApiStorageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    storage_type_id = models.IntegerField()
    type_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'api_storage_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClientContacts(models.Model):
    client_contacts_id = models.AutoField(primary_key=True)
    abc_client = models.ForeignKey(AbcClient, models.DO_NOTHING)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_contacts'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    abc_client = models.ForeignKey(AbcClient, models.DO_NOTHING)
    inventory_name = models.CharField(max_length=45)
    storage_type = models.ForeignKey('StorageType', models.DO_NOTHING)
    max_item_capacity = models.BigIntegerField()
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class ResourceType(models.Model):
    resource_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resource_type'


class StorageType(models.Model):
    storage_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage_type'
