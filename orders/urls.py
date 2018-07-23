from django.urls import path

from orders.views import order_create, AdminOrderDetail, admin_order_detail

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>/', AdminOrderDetail.as_view(), name='admin_order_detail'),
]