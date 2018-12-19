from django.views.generic import ListView, DetailView
from .models import Product, Category, Brand, FeedBack, ProductCharacteristic
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_http_methods
from .forms import FeedBackForm
from django.shortcuts import get_object_or_404
from django.contrib import auth


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
        context['characteristics'] = ProductCharacteristic.objects.filter(
            product_id=self.kwargs['pk']).order_by('characteristic_type')
        context['cart_product_form'] = CartAddProductForm()
        context['product_feedback'] = FeedBack.objects.filter(product_id=self.kwargs['pk'])
        print(context)
        return context


@require_http_methods(['POST'])
def add_comment(request, product):
    form = FeedBackForm(request.POST)
    product = get_object_or_404(Product, id=product)

    if form.is_valid():
        try:
            author = auth.get_user(request)

        except:
            author = None

