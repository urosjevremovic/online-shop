from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from shop.models import Product, Category


class ProductTests(TestCase):

    def setUp(self):

        self.category = Category.objects.create(
            name='tea',
            slug='tea',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='red tea',
            slug='red-tea',
            image='',
            description='Best red tea',
            price=20,
            stock=20,
            available=True,
            created=timezone.now,
            updated=timezone.now
        )

    def test_string_representation(self):
        product = Product(name='red tea')
        self.assertEqual(str(product), product.name)

    def test_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), '/1/red-tea/')

    def test_product_list_without_category_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'red tea')
        self.assertContains(response, 20)
        self.assertTemplateUsed(response, 'shop/product/list.html')

    def test_product_list_with_category_view(self):
        response = self.client.get(reverse('shop:product_list_by_category', args=('tea', )))
        no_response = self.client.get(reverse('shop:product_list_by_category', args=('meat', )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'red tea')
        self.assertContains(response, 'tea')
        self.assertContains(response, 20)
        self.assertTemplateUsed(response, 'shop/product/list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', args=(1, 'red-tea')))
        no_response = self.client.get(reverse('shop:product_detail', args=(20, 'black-tea')))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'red tea')
        self.assertContains(response, 20)
        self.assertContains(response, 'tea')
        self.assertContains(response, 'Quantity')
        self.assertTemplateUsed(response, 'shop/product/detail.html')