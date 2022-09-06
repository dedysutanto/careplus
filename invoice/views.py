from django.shortcuts import render
from invoice.models import Invoices, InvoiceItems
from django.db.models import Sum


def print_invoice(request, invoice_number):
    invoice = Invoices.objects.get(number=invoice_number)
    invoice_item = InvoiceItems.objects.filter(invoice=invoice)
    total = InvoiceItems.objects.filter(invoice=invoice).aggregate(Sum('sub_total'))
    context = {
        'invoice': invoice,
        'invoice_item': invoice_item,
        'total': total['sub_total__sum'],
    }
    return render(request, 'invoice/print.html', context)
