from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from invoice.models import Invoices, InvoiceItems
from django.db.models import Sum
from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


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
