from django.urls import path
from AppeCommerce.views import *

urlpatterns = [
    path('product/', product, name='product'),
    path('category/', category, name='category'),
    path('customer/', customer, name='customer'),
    path('search/', search, name='search'),
]
