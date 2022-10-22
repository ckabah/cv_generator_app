from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', account_activation, name = 'activate'),
    path('login', login_view, name='login'),
]