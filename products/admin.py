from django.contrib import admin
from .models import Product, offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code' , 'discount')

#to add names for the admin product 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'stock')

admin.site.register(offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)

