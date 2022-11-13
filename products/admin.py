from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display= ['title', 'date', 'active', 'content', 'image']
    list_editable= ['active', 'content']
    search_fields=['title']
    list_filter= ['active']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.site_header='Noble'
admin.site.site_title ='Noble'

