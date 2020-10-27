from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone



class RegtFund(models.Model):
	product_name = models.CharField(max_length=150, blank=False, null=False)
	make_and_model = models.CharField(max_length=150 ,blank=False, null=False)
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	purchase_date = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField(blank=False, null=False)
	quantity = models.IntegerField(blank=False, null=False)
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=False, null=False)
	unservicable = models.CharField(max_length=150, blank=False, null=False)
	issue_to_company = models.CharField(max_length=150, blank=False, null=False)
	issue_date = models.DateTimeField(auto_now_add=True)
	product_photo = models.ImageField(upload_to='regt_product_pic/', blank=True, null=True)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	remarks = models.CharField(max_length=150, blank=True, null=True)


class QdFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='qdfund_product_pic/', blank=True, null=True)


class OffrsMessFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='offrs_product_pic/', blank=True, null=True)


class JcoMessFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='jco_product_pic/', blank=True, null=True)



