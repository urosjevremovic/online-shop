from django.urls import path

from payment.views import PaymentDone, PaymentCanceled
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', PaymentDone.as_view(), name='done'),
    path('canceled/', PaymentCanceled.as_view(), name='canceled'),
]