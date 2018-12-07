from django.urls import path

from .views import cart_add, cart_detail, cart_remove

app_name = 'cart'

urlpatterns = [
    path('remove/<product_id>/', cart_remove, name='cart_remove'),
    path('add/<product_id>/', cart_add, name='cart_add'),
    path('', cart_detail, name='cart_detail'),
]