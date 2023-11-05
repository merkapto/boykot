from django.contrib import admin

from .models import Category, Company, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'percentage', 'colored', 'category', )
    list_display_links = ('name',)
    list_filter = ['company', 'category', 'color']
    search_fields = ('name', )




admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Product, ProductAdmin)