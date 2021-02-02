from django.shortcuts import render
from django.views import generic
from shop.models import Product
from shop.forms import SearchForm
from shop import models, forms



class ProductListAll(generic.ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'


    def get_context_data(self, *args, **kwargs):
        object_list = None
        if self.request.GET:
            object_list = self.model.objects.filter(title__contains=self.request.GET.get('search_field'))
        context = super().get_context_data(object_list=object_list, *args, **kwargs)
        context['form'] = SearchForm
        return context






class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'




