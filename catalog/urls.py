from django.urls import path

from .views import ProductDetailView, ProductListView
app_name = 'catalog'

urlpatterns = [
    path('products/<str:slug>/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('products/', ProductListView.as_view(), name='product_list')
]