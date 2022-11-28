# Generated by Django 4.1.3 on 2022-11-28 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abc_client',
            fields=[
                ('abc_client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=45)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='access_log',
            fields=[
                ('access_log_id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=45)),
                ('field_name', models.CharField(max_length=45)),
                ('screen_name', models.CharField(max_length=45)),
                ('table_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('postal_code', models.CharField(max_length=45)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='resource_type',
            fields=[
                ('resource_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=45)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='storage_type',
            fields=[
                ('storage_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=45)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_name', models.CharField(max_length=45)),
                ('max_item_capacity', models.IntegerField()),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
                ('abc_client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abc_client')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('storage_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.storage_type')),
            ],
        ),
        migrations.CreateModel(
            name='client_contacts',
            fields=[
                ('client_contacts_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
                ('abc_client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abc_client')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contact')),
            ],
        ),
        migrations.CreateModel(
            name='abc_resource',
            fields=[
                ('abc_resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_name', models.CharField(max_length=45)),
                ('current_number_of_resources', models.IntegerField()),
                ('max_number_of_resources', models.IntegerField()),
                ('created_by', models.CharField(max_length=45)),
                ('created_date', models.DateField()),
                ('is_deleted', models.BooleanField()),
                ('modified_by', models.CharField(max_length=45)),
                ('modified_date', models.DateField()),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inventory')),
                ('resource_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.resource_type')),
            ],
        ),
        migrations.AddField(
            model_name='abc_client',
            name='company_address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
    ]
