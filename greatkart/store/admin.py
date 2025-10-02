from django.contrib import admin
from .models import Product,Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','price','stock','category','is_available','modified_date','images')
    list_editable = ('price','stock','is_available')
    list_per_page = 20
 
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active','created_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value')
    # list_per_page = 20
        
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
