from django.test import TestCase
from django.urls import reverse


class CartTest(TestCase):

    def setUp(self):
        self.url = reverse('cart:cart_detail')

    def test_cart_detail_view_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/detail.html')
        self.assertInHTML(response, '<a href="/" class="button light">Continue shopping</a>')
