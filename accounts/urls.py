from django.conf.urls import url
from django.urls import path

from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
