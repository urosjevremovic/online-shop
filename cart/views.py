from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, FormView, DeleteView, DetailView
from django.views.generic.base import View

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product


class UpdateCart(FormView):
    http_method_names = ['post', ]
    form_class = CartAddProductForm
    success_url = 'cart:cart_detail'

    def __init__(self):
        super().__init__()
        self.cart = Cart(self.request)

    def form_valid(self, form):
        cd = form.cleaned_data
        self.cart.add(get_object_or_404(Product, id=self.kwargs['product_id']))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


class CartDetail(DetailView):
    model = Cart
    template_name = 'cart/detail.html'
    context_object_name = 'cart'
