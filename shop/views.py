from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cart.forms import CartAddProductForm
from shop.models import Category, Product


class ProductList(ListView):
    model = Product
    template_name = 'shop/product/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = None
        categories = Category.objects.all()
        products = self.get_queryset().filter(available=True)
        if self.kwargs:
            category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
            products = products.filter(category=category)
        context['category'] = category
        context['categories'] = categories
        context['products'] = products
        return context


class ProductDetail(FormMixin, DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = "id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    form_class = CartAddProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_product_form'] = self.form_class
        return context


