from django.db import models
from wagtail.admin.forms import WagtailAdminModelForm
from django.core.exceptions import ValidationError
from doctor.models import Doctors
from account.models import User
from patient.models import Patients, Soaps
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from crum import get_current_user
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel
from django.db.models import Sum
from django.utils.html import format_html


class InvoiceForm(WagtailAdminModelForm):

    class Meta:
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if not instance or not instance.pk:
            initial = kwargs.get('initial', {})
            print(initial)
            user = get_current_user()
            if not user.membership.is_clinic:
                doctor = Doctors.objects.get(user=user)
            initial.update({
                'doctor': doctor
            })
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    '''
    def clean(self):
        cleaned_data = super().clean()

        print(self.formsets)

        for form in self.formsets['related_invoice'].forms:

            print(form)

            if form.is_valid():
                cleaned_form_data = form.clean()

        return cleaned_data
    '''


class Invoices(ClusterableModel, Orderable):
    def limit_choices_to_current_user():
        user = get_current_user()
        if not user.is_superuser:
            return {'user': user}
        else:
            return {}
    number = models.CharField(_('ID'), max_length=16, unique=True)

    patient = ParentalKey(
        Patients,
        on_delete=models.CASCADE,
        limit_choices_to=limit_choices_to_current_user,
        related_name='related_invoice_patient'

    )
    datetime = models.DateTimeField(_('Date Time'), default=now)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    doctor = models.ForeignKey(
        Doctors,
        on_delete=models.RESTRICT,
        verbose_name=_('Doctor'),
        limit_choices_to=limit_choices_to_current_user,
    )

    soap = models.ForeignKey(
        Soaps,
        on_delete=models.CASCADE,
        null=True
    )

    is_final = models.BooleanField(_('Check and Correct'), default=False)
    is_cancel = models.BooleanField(_('Cancel'), default=False)

    is_email = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    panels = [
        FieldRowPanel([FieldPanel('doctor'), FieldPanel('patient'), FieldPanel('datetime')]),
        InlinePanel('related_invoice', heading='Items', label='Detail Item'),
        FieldRowPanel([FieldPanel('is_final'), FieldPanel('is_cancel')]),
    ]

    base_form_class = InvoiceForm

    class Meta:
        db_table = 'invoices'
        verbose_name = 'invoice'
        verbose_name_plural = 'invoices'

    '''
    def clean(self):
        if self.soap is None:
            self.soap = Soaps.objects.filter(
                doctor=self.doctor, patient=self.patient).order_by('datetime', 'number').last()

            if self.soap is None:
                raise ValidationError('Patient is not diagnosed. Please create SOAP for patient')
    '''

    def save(self):
        if self.user is None:
            self.user = get_current_user()

        total = InvoiceItems.objects.filter(invoice=self).aggregate(Sum('sub_total'))
        self.total = total['sub_total__sum']

        if len(str(self.number)) != 16:
            number = Invoices.objects.filter(user=self.user).count() + 1
            prefix = 'INV{:04d}{:02d}'.format(self.user.id, self.doctor.id)
            self.number = '{}{:07d}'.format(prefix, number)
            print('Invoice', self.number)

        if self.soap is None:
            self.soap = Soaps.objects.filter(
                doctor=self.doctor, patient=self.patient).order_by('datetime', 'number').last()

        return super(Invoices, self).save()

    '''
    def clean(self):
        if self.soap is None:
            soap = Soaps.objects.filter(
                doctor=self.doctor, patient=self.patient).order_by('datetime', 'number').last()

            if soap is None:
                raise ValidationError('No SOAP for the patient. Please create SOAP first.')
    '''

    def calculate_total(self):
        total = InvoiceItems.objects.filter(invoice=self).aggregate(Sum('sub_total'))
        return 'Rp. {:,}'.format(total['sub_total__sum']).replace(',', '.')
    calculate_total.short_description = 'Total'

    def patient_number(self):
        return format_html('{}</br>{}', self.patient, self.patient.number)
    patient_number.short_description = _('Patient')

    def get_edit_url(self):
        return "/login/invoices/edit/%i/" % self.id


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
