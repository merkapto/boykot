from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib import admin
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="Category")
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name="Company")
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    color_choices = (
        ("RED", "Red"),
        ("YELLOW", "Yellow"),
        ("GREEN", "Green"),
    )
    
    name = models.CharField(max_length=32, verbose_name="Product")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    percentage = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=32, choices=color_choices, default="RED",  null=True)
    alternative = models.ManyToManyField("self", blank=True)
        
    class Meta:
        ordering = ['name']
    
    @admin.display
    def colored(self):
        return format_html(
            '<b style="color: {};">{}</b>',
            self.color,
            self.color,
        )

    def __str__(self):
        return self.name