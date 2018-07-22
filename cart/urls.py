from django.urls import path

from cart.views import cart_remove, CartDetail, UpdateCart

app_name = 'cart'

urlpatterns = [
    path('', CartDetail.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', UpdateCart.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]