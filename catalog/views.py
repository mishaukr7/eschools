from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Brand
from cart.forms import CartAddProductForm
# Create your views here.


class ProductListView(ListView):
    model = Product
    paginate_by = 9
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProductListView, self).get_context_data(**kwargs)
        data['brands'] = Brand.objects.all()
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def post(self, request, *args, **kwargs):
        return
