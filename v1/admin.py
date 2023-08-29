from django.contrib import admin
from .models import Category,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","inventory"]
    search_fields = ["name","category__name"]
    list_filter = ["category"]
    ordering = ["price"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)