from django.db import models
from django.utils import timezone
from django.db.models import Q

class AtgFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
	             Q(make_and_model__icontains=query)|
	             Q(serial_no__icontains=query)|
	             Q(quantity__icontains=query)|
	             Q(issue_to_company__icontains=query)|
	             Q(issue_date__icontains=query)|
	             Q(return_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(remarks__icontains=query)|
	             Q(company_72_quantity__icontains=query)|
	             Q(company_73_quantity__icontains=query)|
	             Q(company_369_quantity__icontains=query)|
	             Q(company_685PK_quantity__icontains=query)|
	             Q(company_RHQ_quantity__icontains=query)
	        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class AcgFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
	             Q(make_and_model__icontains=query)|
	             Q(serial_no__icontains=query)|
	             Q(quantity__icontains=query)|
	             Q(issue_to_company__icontains=query)|
	             Q(issue_date__icontains=query)|
	             Q(return_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(remarks__icontains=query)|
	             Q(company_72_quantity__icontains=query)|
	             Q(company_73_quantity__icontains=query)|
	             Q(company_369_quantity__icontains=query)|
	             Q(company_685PK_quantity__icontains=query)|
	             Q(company_RHQ_quantity__icontains=query)
	        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs



class FpAndTgFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
	             Q(make_and_model__icontains=query)|
	             Q(serial_no__icontains=query)|
	             Q(quantity__icontains=query)|
	             Q(issue_to_company__icontains=query)|
	             Q(issue_date__icontains=query)|
	             Q(return_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(remarks__icontains=query)|
	             Q(company_72_quantity__icontains=query)|
	             Q(company_73_quantity__icontains=query)|
	             Q(company_369_quantity__icontains=query)|
	             Q(company_685PK_quantity__icontains=query)|
	             Q(company_RHQ_quantity__icontains=query)
	        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class MiscFundManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
            	 Q(product_name__icontains=query)| 
	             Q(make_and_model__icontains=query)|
	             Q(serial_no__icontains=query)|
	             Q(quantity__icontains=query)|
	             Q(issue_to_company__icontains=query)|
	             Q(issue_date__icontains=query)|
	             Q(return_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(annual_stock_taking_date__icontains=query)|
	             Q(remarks__icontains=query)|
	             Q(company_72_quantity__icontains=query)|
	             Q(company_73_quantity__icontains=query)|
	             Q(company_369_quantity__icontains=query)|
	             Q(company_685PK_quantity__icontains=query)|
	             Q(company_RHQ_quantity__icontains=query)
	        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class AtgFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='atgfund_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False, default='0')
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	company_72_quantity = models.IntegerField(blank=True, null=True)
	company_73_quantity = models.IntegerField(blank=True, null=True)
	company_369_quantity = models.IntegerField(blank=True, null=True)
	company_685PK_quantity = models.IntegerField(blank=True, null=True)
	company_RHQ_quantity = models.IntegerField(blank=True, null=True)

	objects = AtgFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


class AcgFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='acgfund_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False, default='0')
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	company_72_quantity = models.IntegerField(blank=True, null=True)
	company_73_quantity = models.IntegerField(blank=True, null=True)
	company_369_quantity = models.IntegerField(blank=True, null=True)
	company_685PK_quantity = models.IntegerField(blank=True, null=True)
	company_RHQ_quantity = models.IntegerField(blank=True, null=True)

	objects = AcgFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


class FpAndTgFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='fptgfund_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False, default='0')
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	company_72_quantity = models.IntegerField(blank=True, null=True)
	company_73_quantity = models.IntegerField(blank=True, null=True)
	company_369_quantity = models.IntegerField(blank=True, null=True)
	company_685PK_quantity = models.IntegerField(blank=True, null=True)
	company_RHQ_quantity = models.IntegerField(blank=True, null=True)

	objects = FpAndTgFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)


class MiscFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='savingsfund_product_pic/', blank=True, null=True)
	make_and_model = models.CharField(max_length=150 ,blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False, default='0')
	balance_in_stock = models.IntegerField(blank=True, null=True)
	servicable = models.CharField(max_length=150 ,blank=True, null=True)
	unservicable = models.CharField(max_length=150, blank=True, null=True)
	issue_to_company = models.CharField(max_length=150, blank=True, null=True)
	issue_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=timezone.now)
	annual_stock_taking_date = models.DateTimeField(default=timezone.now)
	condemnation_date = models.DateTimeField(default=timezone.now)
	company_72_quantity = models.IntegerField(blank=True, null=True)
	company_73_quantity = models.IntegerField(blank=True, null=True)
	company_369_quantity = models.IntegerField(blank=True, null=True)
	company_685PK_quantity = models.IntegerField(blank=True, null=True)
	company_RHQ_quantity = models.IntegerField(blank=True, null=True)

	objects = MiscFundManager()

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)

