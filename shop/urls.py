from django.urls import path

from shop.views import ProductList, ProductDetail

app_name = 'shop'

urlpatterns = [
    path('<slug:category_slug>/', ProductList.as_view(), name='product_list_by_category'),
    path('', ProductList.as_view(), name='product_list'),

    path('<int:id>/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    ]