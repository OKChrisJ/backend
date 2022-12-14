from django.db import models

class address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=45, null=True)
    state = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.address_id)

class storage_type(models.Model):
    storage_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.storage_type_id)

class resource_type(models.Model):
    resource_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.resource_type_id)

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.contact_id)

class abc_client(models.Model):
    abc_client_id = models.AutoField(primary_key=True)
    company_address_id = models.ForeignKey(address, on_delete=models.CASCADE, null=True)
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45, null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.abc_client_id)

class inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    inventory_name = models.CharField(max_length=45)
    abc_client_id = models.ForeignKey(abc_client, on_delete=models.CASCADE)
    address_id = models.ForeignKey(address, on_delete=models.CASCADE, null=True)
    storage_type_id = models.ForeignKey(storage_type, on_delete=models.CASCADE)
    max_item_capacity = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.inventory_id)

class abc_resource(models.Model):
    abc_resource_id = models.AutoField(primary_key=True)
    inventory_id = models.ForeignKey(inventory, on_delete=models.CASCADE)
    resource_type_id = models.ForeignKey(resource_type, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=45)
    current_number_of_resources = models.IntegerField()
    max_number_of_resources = models.IntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.abc_resource_id)

class client_contacts(models.Model):
    client_contacts_id = models.AutoField(primary_key=True)
    abc_client_id = models.ForeignKey(abc_client, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(contact, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=45)
    created_date = models.DateField()
    is_deleted = models.BooleanField()
    modified_by = models.CharField(max_length=45, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return str(self.client_contacts_id)

class access_log(models.Model):
    access_log_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=45)
    field_name = models.CharField(max_length=45, null=True)
    screen_name = models.CharField(max_length=45, null=True)
    table_name = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=45)

    def __str__(self):
        return str(self.access_log_id)