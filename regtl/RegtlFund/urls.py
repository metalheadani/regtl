from django.urls import path
from . import views

app_name='mainapp'

urlpatterns = [
	#path('', views.index, name='index'),
	path('', views.SearchView.as_view(), name='search'),
]
