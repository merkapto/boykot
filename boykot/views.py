from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

from .models import Product, Company, Category

class ProductListView(ListView):
    model = Product
    # template_name = 'product.html'
    def get_queryset(self):
        return Product.objects.all().order_by('?')[:9]
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class ProductDetailView(DetailView):
    model = Product
    slug_field = 'name'
    slug_url_kwarg = 'name'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CompanyListView(ListView):
    model = Company
    def get_queryset(self):
        return Company.objects.all()
    
class CompanyDetailView(DetailView):
    model = Company
    slug_field = 'name'
    slug_url_kwarg = 'name'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryListView(ListView):
    model = Category
    # template_name = 'product.html'
    def get_queryset(self):
        return Category.objects.all()

class SearchListView(ListView):
    model = Product
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(company__name__icontains=query) | Q(category__name__icontains=query)
        )
        return object_list


# class SearchView(ListView):
#     model = Product
#     template_name = 'search.html'
#     # queryset = Talebeler.objects.filter(first_name__icontains='Muhammed')

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Talebeler.objects.filter(
#             Q(first_name__icontains=query) | Q(last_name__icontains=query)
#         )
#         return object_list