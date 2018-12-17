from django.conf.urls import url
from django.urls import path

from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('user_login', views.user_login, name='user_login'),
    # path('login', auth_views.LoginView.as_view(template_name='shop/index.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='shop:home'), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
