from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price',
                     'in_stock']  # will be displayed as form widgets on the change list page, allowing users to edit and save multiple rows at once.
    prepopulated_fields = {
        'slug': ('title',)
        # The main use for this functionality is to automatically generate the value for SlugField fields from one or more other fields.
    }
