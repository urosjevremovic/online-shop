from django.test import TestCase
from django.urls import reverse


class OrderTest(TestCase):

    def setUp(self):
        self.valid_form_data = {
            'first_name': 'Bruno',
            'last_name': 'Mars',
            'email': 'bruno@mars.pl',
            'address': 'Somewhere nr. 5',
            'postal_code': '13213',
            'city': 'Belgrade',
        }

        self.invalid_form_data = {
            'first_name': 'Bruno',
            'last_name': 'Mars',
            'email': 'bruno@mars',
            'address': 'Somewhere nr. 5',
            'postal_code': '13213',
            'city': 'Belgrade',
        }
        self.url = reverse('orders:order_create')

    def test_call_view_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order/create.html')
        self.assertContains(response, 'first_name')

    def test_call_view_fails_with_blank_data(self):
        response = self.client.post(self.url, {})
        self.assertTemplateUsed(response, 'orders/order/create.html')
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')

    def test_call_view_fails_with_invalid_data(self):
        response = self.client.post(self.url, self.invalid_form_data)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_call_view_passes_with_valid_data(self):
        response = self.client.post(self.url, self.valid_form_data, follow=True)
        self.assertRedirects(response, reverse('payment:process'), status_code=302)
