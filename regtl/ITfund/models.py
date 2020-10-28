from django.db import models
from django.utils import timezone


class ItFund(models.Model):
	serial_no = models.CharField(max_length=150 ,blank=False, null=False)
	product_name = models.CharField(max_length=150, blank=False, null=False)
	date_of_procurement = models.DateTimeField(default=timezone.now)
	issued_to = models.CharField(max_length=150, blank=False, null=False)
	remarks = models.CharField(max_length=150, blank=True, null=True)
	picture = models.ImageField(upload_to='itfund_product_pic/', blank=True, null=True)

	def __str__(self):
		return '{}, {}'.format('Serial no: '+self.serial_no, 'Product name: '+self.product_name)

