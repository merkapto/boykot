from django.urls import path

from .views import ProductListView, ProductDetailView, CompanyListView, CompanyDetailView, CategoryListView, SearchListView

app_name = 'boykot'

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('product/<str:name>/', ProductDetailView.as_view(), name="product-detail"),
    
    path('company/', CompanyListView.as_view(), name="company-list"),
    path('company/<str:name>/', CompanyDetailView.as_view(), name="company-detail"),
    
    path('category/', CategoryListView.as_view(), name="category-list"),
    
    path('search/', SearchListView.as_view(), name="search-list"),
]