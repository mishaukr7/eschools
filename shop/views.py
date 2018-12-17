from django.shortcuts import render
from django.views.generic.base import TemplateView
from catalog.models import Product
from .models import News
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_products'] = Product.objects.filter(best=True)
        context['new_products'] = Product.objects.order_by('-created')[:10]
        context['last_news'] = News.objects.order_by('-created')[:3]
        return context

