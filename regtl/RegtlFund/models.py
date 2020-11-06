from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone


from django.db.models import Q

class RegtFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
	             Q(make_and_model__icontains=query)|
	             Q(serial_no__icontains=query)|
	             Q(purchase_date__icontains=query)|
	             Q(quantity__icontains=query)|
	             Q(issue_to_company__icontains=query)|
	             Q(issue_date__icontains=query)|
	             Q(return_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(remarks__icontains=query)
	        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class QdFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
                 Q(make_and_model__icontains=query)|
                 Q(serial_no__icontains=query)|
                 Q(purchase_date__icontains=query)|
                 Q(quantity__icontains=query)|
                 Q(issue_to_company__icontains=query)|
                 Q(issue_date__icontains=query)|
                 Q(return_date__icontains=query)|
                 Q(annual_stock_taking_date__icontains=query)|
                 Q(annual_stock_taking_date__icontains=query)|
                 Q(remarks__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class OffrsMessFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(product_name__icontains=query)| 
                         Q(make_and_model__icontains=query)|
                         Q(serial_no__icontains=query)|
                         Q(purchase_date__icontains=query)|
                         Q(quantity__icontains=query)|
                         Q(issue_to_company__icontains=query)|
                         Q(issue_date__icontains=query)|
                         Q(return_date__icontains=query)|
                         Q(annual_stock_taking_date__icontains=query)|
                         Q(annual_stock_taking_date__icontains=query)|
                         Q(remarks__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class JcoFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(product_name__icontains=query)| 
                         Q(make_and_model__icontains=query)|
                         Q(serial_no__icontains=query)|
                         Q(purchase_date__icontains=query)|
                         Q(quantity__icontains=query)|
                         Q(issue_to_company__icontains=query)|
                         Q(issue_date__icontains=query)|
                         Q(return_date__icontains=query)|
                         Q(annual_stock_taking_date__icontains=query)|
                         Q(annual_stock_taking_date__icontains=query)|
                         Q(remarks__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class RegtFund(models.Model):
	product_name = models.CharField(max_length=150, blank=False, null=False, default='0')
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	serial_no = models.CharField(max_length=150 ,blank=False, null=False, default='0')
	purchase_date = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField(blank=False, null=False, default='0')
	quantity = models.IntegerField(blank=False, null=False, default='0')
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=False, null=False, default='0')
	unservicable = models.CharField(max_length=150, blank=False, null=False, default='0')
	issue_to_company = models.CharField(max_length=150, blank=False, null=False, default='0')
	issue_date = models.DateTimeField(auto_now_add=True)
	product_photo = models.ImageField(upload_to='regt_product_pic/', blank=True, null=True)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	remarks = models.CharField(max_length=150, blank=True, null=True)

	objects = RegtFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


class QdFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	purchase_date = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	product_photo = models.ImageField(upload_to='qdfund_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False)
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)

	objects = QdFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


class OffrsMessFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	purchase_date = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	product_photo = models.ImageField(upload_to='offrs_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False)
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)

	objects = OffrsMessFundManager()


	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


		
class JcoMessFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	purchase_date = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	product_photo = models.ImageField(upload_to='jco_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False)
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)

	objects = JcoFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)

