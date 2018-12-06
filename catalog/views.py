from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category
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
