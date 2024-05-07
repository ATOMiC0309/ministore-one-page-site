from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'get_image')
    list_display_links = ('pk', 'name')

    def get_image(self, category):
        return mark_safe(f'<img src="{category.image.url}" style="width: 80px" alt="Image not found"/>')

    get_image.short_description = "Image"

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmi(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'slug', 'get_image')
    list_display_links = ('pk', 'name')

    def get_image(self, product):
        return mark_safe(f'<img src="{product.image.url}" style="width: 80px" alt="Image not found"/>')

    get_image.short_description = "Image"
