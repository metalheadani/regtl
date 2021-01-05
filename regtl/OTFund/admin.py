from django.contrib import admin
from django.contrib.admin import site
from .models import *

class AtgFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class AcgFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class FpAndTgFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class MiscFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


admin.site.register(AtgFund)
admin.site.register(AcgFund)
admin.site.register(FpAndTgFund)
admin.site.register(MiscFund)
