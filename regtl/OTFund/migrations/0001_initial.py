# Generated by Django 3.1.2 on 2020-11-06 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcgFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='acgfund_product_pic/')),
                ('make_and_model', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(default='0')),
                ('balance_in_stock', models.IntegerField(blank=True, null=True)),
                ('servicable', models.CharField(blank=True, max_length=150, null=True)),
                ('unservicable', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_to_company', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('annual_stock_taking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condemnation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AtgFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='atgfund_product_pic/')),
                ('make_and_model', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(default='0')),
                ('balance_in_stock', models.IntegerField(blank=True, null=True)),
                ('servicable', models.CharField(blank=True, max_length=150, null=True)),
                ('unservicable', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_to_company', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('annual_stock_taking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condemnation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FpAndTgFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='fptgfund_product_pic/')),
                ('make_and_model', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(default='0')),
                ('balance_in_stock', models.IntegerField(blank=True, null=True)),
                ('servicable', models.CharField(blank=True, max_length=150, null=True)),
                ('unservicable', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_to_company', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('annual_stock_taking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condemnation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('date_of_procurement', models.DateTimeField(default=django.utils.timezone.now)),
                ('issued_to', models.CharField(max_length=150)),
                ('remarks', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='savingsfund_product_pic/')),
                ('make_and_model', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(default='0')),
                ('balance_in_stock', models.IntegerField(blank=True, null=True)),
                ('servicable', models.CharField(blank=True, max_length=150, null=True)),
                ('unservicable', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_to_company', models.CharField(blank=True, max_length=150, null=True)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('annual_stock_taking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condemnation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
