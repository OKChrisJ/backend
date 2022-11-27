from django.db import models

class abc_client(models.Model):
    abc_client_id = models.AutoField(primary_key=True)
    company_address_id = models.ForeignKey(address.address_id, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField(primary_key=True)
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class abc_resource(models.Model):
    abc_resource_id = models.AutoField(primary_key=True)
    inventory_id = models.ForeignKey(inventory.inventory_id, on_delete=models.CASCADE)
    resource_type_id = models.ForeignKey(resource_type.resource_type_id, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=45)
    current_number_of_resources = models.IntegerField()
    max_number_of_resources = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class access_log(models.Model):
    access_log_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=45)
    field_name = models.CharField(max_length=45)
    screen_name = models.CharField(max_length=45)
    table_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)

class address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class client_contacts(models.Model):
    client_contacts_id = models.AutoField(primary_key=True)
    abc_client_id = models.ForeignKey(abc_client.abc_client_id, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(contact.contact_id, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    inventory_name = models.CharField(max_length=45)
    abc_client_id = models.ForeignKey(abc_client.abc_client_id, on_delete=models.CASCADE)
    address_id = models.IntegerField()
    storage_type_id = models.ForeignKey(storage_type.storage_type_id, on_delete=models.CASCADE)
    max_item_capacity = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class resource_type(models.Model):
    resource_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

class storage_type(models.Model):
    storage_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45)
    modified_date = models.DateField()

