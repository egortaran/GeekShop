from django.urls import path
from adminapp.views import(
    UserListView,
    UserCreateView,
    user_update,
    user_delete,

    products,
    ProductDetailView,
    product_create,
    product_update,
    product_delete,

    categories,
    category_create,
    ProductCategoryUpdateView,
    ProductCategoryDelete,
)

app_name = 'adminapp'

urlpatterns = [
    # users
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),

    # categories
    path('categories/create/', category_create, name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', ProductCategoryDelete.as_view(), name='category_delete'),

    # products
    path('products/create/category/<int:pk>/', product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/<int:pk>/', ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]
