from django.contrib import admin
from catalog.models import Category, Product, ProductCharacteristic, ProductImage, Partner
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource


admin.site.register(Category, MPTTModelAdmin)


class ProductInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 2


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['category', 'brand', 'name', 'description', 'price',
                    'price_with_discount', 'created', 'updated', 'review_video', 'available',
                    'partner']
    list_filter = ['name', 'created']
    inlines = [ProductInline, ProductImageInline]
    resource_class = ProductResource


admin.site.register(Product, ProductAdmin)

admin.site.register(Partner)


# @admin.register(Product)
# class ProductExport(ImportExportModelAdmin):
#     pass
