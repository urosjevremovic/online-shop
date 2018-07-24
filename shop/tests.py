from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from shop.models import Product, Category


class ProductTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@testme.com',
            password='secret',
        )

        self.category = Category.objects.create(
            name='tea',
            slug='tea',
        )

        self.product = Product.objects.create(
            category=self.category,
            name='red tea',
            slug='red_tea',
            image='',
            description='Best red tea',
            price=20,
            stock=20,
            available=True,
            created=timezone.now,
            updated=timezone.now
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'red tea')
        self.assertContains(response, 20)
        self.assertTemplateUsed(response, 'shop/product/list.html')
        response = self.client.get(reverse('shop:product_list_by_category', args=(self.category.slug, )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'red tea')
        self.assertContains(response, 'tea')
        self.assertContains(response, 20)
        self.assertTemplateUsed(response, 'shop/product/list.html')
