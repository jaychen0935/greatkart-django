from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','price','stock','category','is_available','modified_date','images')
    list_editable = ('price','stock','is_available')
    list_per_page = 20
    
admin.site.register(Product,ProductAdmin)