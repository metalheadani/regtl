from django.contrib import admin
from django.contrib.admin import site
from .models import *

class RegtFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class QdFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class OffrsMessFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class JcoMessFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')

class EmptyFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class LRWFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class OTFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


class REGTQMFundAdmin(admin.ModelAdmin):
	search_fields = ['serial_no', 'product_name','issued_to','remarks']
	list_display = ('serial_no','product_name','issued_to')


admin.site.register(RegtFund)
admin.site.register(QdFund)
admin.site.register(OffrsMessFund)
admin.site.register(JcoMessFund)
admin.site.register(EmptyFund)
admin.site.register(LRWFund)
admin.site.register(OTFund)
admin.site.register(REGTQMFund)