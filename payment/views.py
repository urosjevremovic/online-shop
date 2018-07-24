from io import BytesIO

import braintree
import weasyprint
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from online_shop.settings import EMAIL_HOST_USER
from orders.models import Order


def payment_process(request): 
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            # create invoice e-mail
            subject = 'Online Shop - Invoice no. {}'.format(order.id)
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject, message, 'urosh43@gmail.com', [order.email])
            # generate PDF
            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
            # attach PDF file
            email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
            # send e-mail
            # send_mail(subject, message, 'urosh43@gmail.com', [order.email])
            email.send()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token})


class PaymentDone(TemplateView):
    template_name = 'payment/done.html'


class PaymentCanceled(TemplateView):
    template_name = 'payment/canceled.html'