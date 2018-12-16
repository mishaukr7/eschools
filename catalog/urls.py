from django.urls import path

from .views import ProductDetailView
app_name = 'catalog'

urlpatterns = [
    path('products/<slug:slug>/<int:pk>', ProductDetailView.as_view(), name='product'),
    # path('products/', )
]