from django.urls import path, re_path
from .views import products, product
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('product/<int:pk>/', product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/$', cache_page(3600)(products)),
]
