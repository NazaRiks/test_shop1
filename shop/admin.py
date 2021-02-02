from django.contrib import admin
from .models import  Product, Category, Comment




class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'slug', 'price', 'available', 'category', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}





admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
