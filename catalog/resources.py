from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Product, ProductCharacteristic, Category, Brand
from django.utils.encoding import force_text
import tablib.core
from django.db.models.query import QuerySet


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, )
    )

    brand = fields.Field(
        column_name='brand',
        attribute='column',
        widget=ForeignKeyWidget(Brand)
    )

    class Meta:
        model = Product
        exclude = ['slug']

    # def get_export_headers(self):
    #     headers = [
    #         force_text(field.column_name) for field in self.get_export_fields()]
    #     return headers
    #
    # def export(self, queryset=None, *args, **kwargs):
    #     """
    #     Exports a resource.
    #     """
    #     self.before_export(queryset, *args, **kwargs)
    #
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #
    #     headers = self.get_export_headers()
    #     headers.append('characteristic_name_1')
    #     data = tablib.Dataset()
    #     data.headers = headers
    #     if isinstance(queryset, QuerySet):
    #         iterable = queryset.iterator()
    #     else:
    #         iterable = queryset
    #     for obj in iterable:
    #
    #         # characteristics = ProductCharacteristic.objects.filter(product_id=obj.id)
    #         # characteristics = characteristics.values_list('id', 'characteristic_type', 'name', 'value')
    #
    #         # for i, characteristic in enumerate(characteristics, 1):
    #         # obj.__setattr__('characteristic_name_1', '1')
    #         # print(obj.__dir__())
    #         obj.characteristic_name_1 = '1'
    #         print(data.headers)
    #
    #         data.append(self.export_resource(obj))
    #
    #         print(data)
    #
    #     self.after_export(queryset, data, *args, **kwargs)
    #
    #     return data

        # super(ProductResource, self).export(queryset=None, *args, **kwargs)


