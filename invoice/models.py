from django.db import models
from django.contrib.auth.models import User
from patient.models import Patients
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from django.utils.translation import gettext as _
from django.utils.timezone import now
from crum import get_current_user
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, HelpPanel
from django.db.models import Sum


class Invoices(ClusterableModel):
    patient = models.ForeignKey(
        Patients,
        on_delete=models.CASCADE,
    )
    datetime = models.DateTimeField('Date Time', default=now)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    panels = [
        FieldRowPanel([FieldPanel('patient'), FieldPanel('datetime')]),
        InlinePanel('related_invoice', heading='Item', label='Detail Item',
                    min_num=None, max_num=None),
    ]

    class Meta:
        db_table = 'invoices'

    def save(self):
        if self.user is None:
            self.user = get_current_user()

        total = InvoiceItems.objects.filter(invoice=self).aggregate(Sum('sub_total'))
        self.total = total['sub_total__sum']

        return super(Invoices, self).save()

    def calculate_total(self):
        total = InvoiceItems.objects.filter(invoice=self).aggregate(Sum('sub_total'))
        return total['sub_total__sum']
    calculate_total.short_description = 'Total'

class InvoiceItems(Orderable):
    item = models.CharField(max_length=50, verbose_name=_('Item'))
    quantity = models.IntegerField(default=1)
    cost = models.IntegerField()
    sub_total = models.IntegerField()

    invoice = ParentalKey('Invoices', on_delete=models.CASCADE, related_name='related_invoice')

    panels = [
        FieldRowPanel([FieldPanel('item'), FieldPanel('quantity'), FieldPanel('cost')])
    ]

    class Meta:
        db_table = 'invoice_items'

    def save(self):
        self.sub_total = self.quantity * self.cost
        return super(InvoiceItems, self).save()
