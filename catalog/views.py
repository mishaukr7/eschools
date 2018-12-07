from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.forms import CartAddProductForm
# Create your views here.


class ProductListView(ListView):
    model = Product
    paginate_by = 9

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        search = self.request.GET.get('q', None)
        filter = self.request.GET.get()
        queryset = Product.objects.all()
        if category_slug is not None:
            queryset = queryset.filter(category__slug=self.kwargs['slug'])

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['categories'] = category.get_slug_list()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def post(self, request, *args, **kwargs):
        return
