from django.contrib import admin
from orders.models import OrderItem, Order
from import_export.admin import ImportExportModelAdmin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(ImportExportModelAdmin):

    list_display = ['customer', 'customer_email', 'customer_phone', 'city', 'delivery_type',
                    'customer_first_name', 'customer_last_name', 'customer_patronymic', 'status',
                    'created']
    list_filter = ['status', 'created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


