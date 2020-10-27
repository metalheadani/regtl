from django.shortcuts import render


def index(request):
	template_name = 'mainapp/index.html'
	context = {}
	return render(request, template_name, context)


def regtFund(request):
	template_name = 'mainapp/regtfund.html'
	context = {}
	return render(request, template_name, context)


def qtFund(request):
	template_name = 'mainapp/qtfund.html'
	context = {}
	return render(request, template_name, context)



def officersMessFund(request):
	template_name = 'mainapp/offersmessfund.html'
	context = {}
	return render(request, template_name, context)


def JCOMessFund(request):
	template_name = 'mainapp/jcomessfund.html'
	context = {}
	return render(request, template_name, context)

