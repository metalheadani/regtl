from django.urls import path
from . import views

app_name='mainapp'

urlpatterns = [
	path('', views.index, name='index'),
	path('regt-fund', views.regtFund, name='regtFund'),
	path('qt-fund', views.qtFund, name='qtFund'),
	path('officers-mess-fund', views.officersMessFund, name='officersMessFund'),
	path('jco-fund', views.JCOMessFund, name='JCOMessFund'),
]

