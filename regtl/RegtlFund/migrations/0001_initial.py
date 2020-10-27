# Generated by Django 3.1.2 on 2020-10-27 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JcoMessFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='jco_product_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='OffrsMessFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='offrs_product_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='QdFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='qdfund_product_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='RegtFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('make_and_model', models.CharField(max_length=150)),
                ('serial_no', models.CharField(max_length=150)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('balance_in_stock', models.IntegerField(blank=True, null=True)),
                ('servicable', models.CharField(max_length=150)),
                ('unservicable', models.CharField(max_length=150)),
                ('issue_to_company', models.CharField(max_length=150)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('product_photo', models.ImageField(blank=True, null=True, upload_to='regt_product_pic/')),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('annual_stock_taking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condemnation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
