from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from orders.views import order_create, AdminOrderDetail, admin_order_pdf

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>/', staff_member_required(AdminOrderDetail.as_view()), name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', admin_order_pdf, name='admin_order_pdf'),
]