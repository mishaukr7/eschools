from django.contrib import admin
from catalog.models import Brand, Category, Product, ProductCharacteristic, ProductImage, Partner, FeedBack
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from .resources import ProductResource
from import_export.formats import base_formats

EXPORT_FORMATS = (
        base_formats.CSV,
        base_formats.XLS,
        base_formats.ODS,
        base_formats.JSON,
        base_formats.HTML,
    )


class ProductInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 2


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(ImportExportModelAdmin):
    #   prepopulated_fields = {"slug": ("name", )}
    list_display = ['id', 'name', 'product_code', 'category', 'brand', 'description', 'price',
                    'price_with_discount', 'created', 'updated', 'review_video', 'available',
                    'partner']
    list_filter = ['name', 'created']
    inlines = [ProductInline, ProductImageInline]
    resource_class = ProductResource
    exclude = ['slug']
    formats = EXPORT_FORMATS


admin.site.register(Product, ProductAdmin)


class ProductCharacteristicAdmin(ImportExportModelAdmin):
    list_filter = ['product', 'name']
    list_display = ['product']
    formats = EXPORT_FORMATS


admin.site.register(ProductCharacteristic, ProductCharacteristicAdmin)


# class CategoryAdmin(ImportExportModelAdmin):
    # formats = EXPORT_FORMATS


class BrandAdmin(ImportExportModelAdmin):
    formats = EXPORT_FORMATS


admin.site.register(Brand, BrandAdmin)


class PartnerAdmin(ImportExportModelAdmin):
    formats = EXPORT_FORMATS


admin.site.register(Partner, PartnerAdmin)


class CategoryAdmin(MPTTModelAdmin):
    exclude = ['slug', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(FeedBack)
