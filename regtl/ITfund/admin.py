from django.contrib import admin
from django.contrib.admin import site
from .models import *

class ItFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	#empty_value_display = '-empty-'
	list_display = ('serial_no','product_name','issued_to')

admin.site.register(ItFund)
