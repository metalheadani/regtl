from django.shortcuts import render
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView
from .models import *
from OTFund.models import AtgFund, AcgFund, FpAndTgFund, MiscFund
from ITfund.models import ItFund

def index(request):
	template_name = 'RegtlFund/index.html'
	context = {}
	return render(request, template_name, context)


class SearchView(ListView):
    template_name = 'RegtlFund/search.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            regtfund_results = RegtFund.objects.search(query)
            qdfund_results = QdFund.objects.search(query)
            offfsmess_results = OffrsMessFund.objects.search(query)
            jcomess_results = JcoMessFund.objects.search(query)
            acg_results = AcgFund.objects.search(query)
            atg_results = AtgFund.objects.search(query)
            fptg_results = FpAndTgFund.objects.search(query)
            savings_results = MiscFund.objects.search(query)
            it_results = ItFund.objects.search(query)
            
            # combine querysets 
            queryset_chain = chain(
                    regtfund_results,
                    qdfund_results,
                    offfsmess_results,
                    jcomess_results,
                    acg_results,
                    atg_results,
                    fptg_results,
                    savings_results,
                    it_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        #return HttpResponse("No results found")
        return RegtFund.objects.none() # just an empty queryset as default


