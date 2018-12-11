from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Product, Category
from django.http import HttpResponse


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'id')
    )

    class Meta:
        model = Product


def export_product_csv(request):
    product_resources = ProductResource()
    dataset = product_resources.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    return response
