# Generated by Django 3.1.2 on 2020-10-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITfund', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itfund',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='itfund_product_pic/'),
        ),
    ]
