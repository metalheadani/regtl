# Generated by Django 3.1.2 on 2020-10-27 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItFund',
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
    ]
