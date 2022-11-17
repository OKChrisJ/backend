from django.db import models

class abc_client(models.Model):
    abc_client_id = models.IntegerField()
    client_name = models.CharField(max_length=100)
    company_address_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    phone_number = models.CharField(max_length=45)

class abc_resource(models.Model):
    abc_resource_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    current_number_of_resources = models.IntegerField()
    inventory_id = models.IntegerField()
    is_deleted = models.BooleanField()
    max_number_of_resources = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    resource_name = models.CharField(max_length=45)
    resource_type_id = models.IntegerField()

class access_log(models.Model):
    access_log_id = models.IntegerField()
    action = models.CharField(max_length=45)
    field_name = models.CharField(max_length=45)
    screen_name = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)

class address(models.Model):
    address_id = models.IntegerField()
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    postal_code = models.CharField(max_length=45)
    state = models.CharField(max_length=45)

class client_contacts(models.Model):
    abc_client_id = models.IntegerField()
    client_contacts_id = models.IntegerField()
    contact_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class contact(models.Model):
    contact_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    email_address = models.EmailField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=50)
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    phone_number = models.CharField(max_length=20)

class inventory(models.Model):
    abc_client_id = models.IntegerField()
    address_id = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    inventory_id = models.IntegerField()
    inventory_name = models.CharField(max_length=45)
    is_deleted = models.BooleanField()
    max_item_capacity = models.IntegerField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    storage_type_id = models.IntegerField()

class resource_type(models.Model):
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    resource_type_id = models.IntegerField()
    type_name = models.CharField(max_length=45)

class storage_type(models.Model):
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()
    storage_type_id = models.IntegerField()
    type_name = models.CharField(max_length=45)

