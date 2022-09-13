from django.db import models
from wagtail.admin.forms import WagtailAdminModelForm
from doctor.models import Doctors
from account.models import User
from modelcluster.models import ClusterableModel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from django.utils.timezone import now, localtime
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, HelpPanel
from crum import get_current_user
from wagtail.admin import widgets
from config.utils import calculate_age
from django.core.exceptions import ObjectDoesNotExist
from config.utils import time_different
from django.utils.html import format_html
from data_support.models import BPJSCodes


SOAP = """S:
O:
A:
P:"""

HELP_PANEL_1 = '<strong>KE</strong>: Karies Email; ' \
               '<strong>KD</strong>: Karies Dentin; ' \
               '<strong>KP</strong>: Karies Menuju Pulpa; ' \
               '<strong>RG</strong>: Radang Gusi ' \
               '<strong>AF</strong>: Amalgam Filling '
HELP_PANEL_2 = '<strong>CF</strong>: Composite Filling; ' \
               '<strong>GR</strong>: Gangren Radix; ' \
               '<strong>GP</strong>: Gangren Pulpa; ' \
               '<strong>PL</strong>: Premature Loss; ' \
               '<strong>IM</strong>: Impaksi '
HELP_PANEL_3 = '<strong>In</strong>: Inlay; ' \
               '<strong>On</strong>: Onlay; ' \
               '<strong>Ab</strong>: Abses; ' \
               '<strong>Cr</strong>: Crown; ' \
               '<strong>Br</strong>: Bridge; ' \
               '<strong>Ve</strong>: Veneer; ' \
               '<strong>M</strong>: Missing; ' \
               '<strong>P</strong>: Persistensi'


GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]

TEETH = [
    (None, '--'),
    ('KE', 'KE'),
    ('KD', 'KD'),
    ('KP', 'KP'),
    ('RG', 'RG'),
    ('AF', 'AF'),
    ('CF', 'CF'),
    ('GR', 'GR'),
    ('GP', 'GP'),
    ('PL', 'PL'),
    ('IM', 'IM'),
    ('In', 'In'),
    ('On', 'On'),
    ('Ab', 'Ab'),
    ('Cr', 'Cr'),
    ('Br', 'Br'),
    ('Ve', 'Ve'),
    ('M', 'M'),
    ('P', 'P'),
]

teeth_right_panels = [
    FieldPanel('patient'),
    FieldRowPanel([
        FieldPanel('eight'),
        FieldPanel('seven'),
        FieldPanel('six'),
        FieldPanel('five'),
        FieldPanel('four'),
        FieldPanel('three'),
        FieldPanel('two'),
        FieldPanel('one'),
    ]),
    FieldRowPanel([
        FieldPanel('m_five'),
        FieldPanel('m_four'),
        FieldPanel('m_three'),
        FieldPanel('m_two'),
        FieldPanel('m_one'),
    ]),
]

teeth_left_panels = [
    FieldPanel('patient'),
    FieldRowPanel([
        FieldPanel('one'),
        FieldPanel('two'),
        FieldPanel('three'),
        FieldPanel('four'),
        FieldPanel('five'),
        FieldPanel('six'),
        FieldPanel('seven'),
        FieldPanel('eight'),
    ]),
    FieldRowPanel([
        FieldPanel('m_one'),
        FieldPanel('m_two'),
        FieldPanel('m_three'),
        FieldPanel('m_four'),
        FieldPanel('m_five'),
    ]),
]


class SoapForm(WagtailAdminModelForm):

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


class PatientForm(WagtailAdminModelForm):

    class Meta:
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        #loop over linked orderables
        #print(self.formsets)
        #print(self.formsets['related_invoice_patient'].forms)
        for form in self.formsets['related_invoice_patient'].forms:

            #check first if form is valid, otherwise cleaned_data will not be accesible/set


            if form.is_valid():
                cleaned_form_data = form.clean()
                #patient = cleaned_form_data.get('patient')
                doctor = cleaned_form_data.get('doctor')
                soap = cleaned_form_data.get('soap')

                #print('PATIENT', patient)
                print('DOCTOR', doctor)
                print('SOAP', soap)

                #execute some validation condition, and raise the error if it fails
                if soap is None:
                    form.add_error('doctor', 'please dont leave me empty')
            #else:
            #    form.add_error('please dont leave me empty')
        return cleaned_data


class Patients(ClusterableModel):
    number = models.CharField(_('ID'), max_length=16, unique=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    gender = models.CharField(max_length=3, verbose_name=_('Gender'), choices=GENDER, default='M')
    dob = models.DateField(verbose_name=_('Date of Birth'))
    address = models.TextField(verbose_name=_('Address'), blank=True, null=True)
    phone = models.CharField(max_length=50, verbose_name=_('Telephone/HP'), blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    is_bpjs = models.BooleanField(_('BPJS'), default=False)
    nik = models.CharField(_('NIK'), max_length=20, blank=True, null=True)
    bpjs_number = models.CharField(_('BPJS Number'), max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    date_widget = widgets.AdminDateInput(
        attrs={
            'placeholder': 'yyyy-mm-dd'
        }
    )

    #base_form_class = PatientForm

    panels = [
        InlinePanel('related_patient',
                    heading="Related SOAP",
                    label="Detail SOAP",),

        InlinePanel('next_appointment',
                    heading='Next Visit',
                    label='Appointment',
                    classname='collapsed',
                    min_num=0, max_num=1),
        InlinePanel('related_invoice_patient',
                    heading='Invoices',
                    label='Invoice',
                    classname='collapsed',),
        MultiFieldPanel([
            FieldPanel('is_bpjs'),
            FieldRowPanel([FieldPanel('name'), FieldPanel('gender')]),
            FieldPanel('dob', widget=date_widget),
            FieldRowPanel([FieldPanel('phone'), FieldPanel('email')]),
            FieldPanel('address')],
            heading='Data Patient'
        ),
        MultiFieldPanel([
           FieldRowPanel([FieldPanel('nik'), FieldPanel('bpjs_number')], classname='collapsed'),
        ]),

        MultiFieldPanel([
            HelpPanel(content=HELP_PANEL_1,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            HelpPanel(content=HELP_PANEL_2,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            HelpPanel(content=HELP_PANEL_3,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            InlinePanel('teeth_upper_right', heading='Upper Right', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
            InlinePanel('teeth_upper_left', heading='Upper Left', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
        ], heading='Upper Teeth Condition', classname="collapsed"),
        MultiFieldPanel([
            HelpPanel(content=HELP_PANEL_1,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            HelpPanel(content=HELP_PANEL_2,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            HelpPanel(content=HELP_PANEL_3,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            InlinePanel('teeth_lower_right', heading='Lower Right', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
            InlinePanel('teeth_lower_left', heading='Lower Left', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
        ], heading='Lower Teeth Condition', classname="collapsed"),

    ]

    class Meta:
        db_table = 'patients'
        verbose_name = 'patient'
        verbose_name_plural = 'patients'

    def __str__(self):
        return '%s' % self.name

    def save(self):
        if self.user is None:
            self.user = get_current_user()

        self.name = self.name.upper()
        self.address = self.address.upper()

        if len(str(self.number)) != 16:
            number = Patients.objects.filter(user=self.user).count() + 1
            prefix = 'MR{:04d}'.format(self.user.id)
            self.number = '{}{:010d}'.format(prefix, number)
            print('Medical Record', self.number)

        '''
        try:
            self.number
            print('Number Exist', self.number)

            if 'MR1' not in self.number:
                self.number = 'MR1' + self.number
        except ObjectDoesNotExist:
            print('Number', self.number)
            number = Patients.objects.count() + 1
            self.number = 'MR1{:08d}'.format(number)
        '''

        return super(Patients, self).save()

    def calculate_age(self):
        '''

        today = date.today()
        try:
            age = (today.year - self.dob.year) \
                  - ((today.month, today.day) < (self.dob.month, self.dob.day))
        except ValueError:
            age = 0
        #return '%d' % age
        '''
        return '%d' % calculate_age(self.dob)

    calculate_age.short_description = _('Age')

    def next_visit(self):
        try:
            next_v = NextAppointment.objects.get(patient=self)
            from datetime import datetime
            return format_html('{}<br />( {} )',
                               localtime(next_v.datetime).strftime("%A %d %b %Y, %H:%M"),
                               time_different(next_v.datetime)
                               )

        except ObjectDoesNotExist:
            return '%s' % _('No appointment')

    next_visit.short_description = _('Next Visit')


class Soaps(Orderable):
    def limit_choices_to_current_user():
        user = get_current_user()
        if not user.is_superuser:
            return {'user': user}
        else:
            return {}

    number = models.CharField(_('ID'), max_length=16, unique=True)
    doctor = models.ForeignKey(
        Doctors,
        on_delete=models.RESTRICT,
        verbose_name=_('Doctor'),
        limit_choices_to=limit_choices_to_current_user,
    )
    datetime = models.DateTimeField(_('Date Time'), default=now)
    subjective = models.TextField(_('Subjective'))
    objective = models.TextField(_('Objective'))
    assessment = models.TextField(_('Assessment'))
    plan = models.TextField(_('Plan'))
    assessment_bpjs = models.ForeignKey(
        BPJSCodes,
        on_delete=models.SET_NULL,
        verbose_name=_('Assessment BPJS'),
        blank=True,
        null=True
    )

    additional_info = models.TextField(verbose_name=_('Additional Information'), blank=True, null=True)
    patient = ParentalKey(
        'Patients',
        on_delete=models.CASCADE,
        related_name='related_patient',
        limit_choices_to=limit_choices_to_current_user,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    image = models.ImageField(upload_to='soap/images', blank=True, null=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    base_form_class = SoapForm

    panels = [
        FieldRowPanel([FieldPanel('doctor'), FieldPanel('patient'), FieldPanel('datetime')]),
        MultiFieldPanel([
            FieldPanel('subjective'),
            FieldPanel('objective'),
            FieldPanel('assessment'),
            FieldPanel('assessment_bpjs'),
            FieldPanel('plan'),
        ], heading='SOAP'),
        FieldPanel('additional_info'),
        FieldPanel('image'),
    ]

    class Meta:
        db_table = 'soaps'
        verbose_name = 'SOAP'
        verbose_name_plural = 'SOAP'
        ordering = ['-datetime']

    def clean(self):
        if self.assessment is None:
            self.assessment = self.assessment_bpjs

    def save(self):
        if self.user is None:
            self.user = get_current_user()

        if len(str(self.number)) != 16:
            number = Soaps.objects.filter(user=self.user, doctor=self.doctor, patient=self.patient).count() + 1
            prefix = 'SOAP{:04d}{:02d}{:03}'.format(self.user.id, self.doctor.id, self.patient.id)
            self.number = '{}{:03d}'.format(prefix, number)
            print('SOAP', self.number)
        return super(Soaps, self).save()

    def image_thumb(self):
        try:
            self.image.url
            if self.image is not None:
                return format_html(
                    '<a href="{}"><img src="{}" width=80, height=80>', self.image.url, self.image.url
                )
            else:
                return None
        except ValueError:
            return None
    image_thumb.short_description = _('Image')


class Teeth(models.Model):
    one = models.CharField('1', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    two = models.CharField('2', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    three = models.CharField('3', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    four = models.CharField('4', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    five = models.CharField('5', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    six = models.CharField('6', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    seven = models.CharField('7', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    eight = models.CharField('8', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    m_one = models.CharField('I', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    m_two = models.CharField('II', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    m_three = models.CharField('III', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    m_four = models.CharField('IV', max_length=2, blank=True, null=True, choices=TEETH, default=None)
    m_five = models.CharField('V', max_length=2, blank=True, null=True, choices=TEETH, default=None)

    class Meta:
        abstract = True


class TeethUpperRight(Orderable, Teeth):
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='teeth_upper_right')

    panels = teeth_right_panels

    class Meta:
        db_table = 'teeth_upper_right'


class TeethUpperLeft(Orderable, Teeth):
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='teeth_upper_left')

    panels = teeth_left_panels

    class Meta:
        db_table = 'teeth_upper_left'


class TeethLowerRight(Orderable, Teeth):
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='teeth_lower_right')

    panels = teeth_right_panels

    class Meta:
        db_table = 'teeth_lower_right'


class TeethLowerLeft(Orderable, Teeth):
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='teeth_lower_left')

    panels = teeth_left_panels

    class Meta:
        db_table = 'teeth_lower_left'


class NextAppointment(Orderable):
    datetime = models.DateTimeField(_('Date Time'), null=True, blank=True)
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='next_appointment')

    panels = [FieldPanel('datetime')]

    class Meta:
        db_table = 'next_appointment'

'''
class MedicalImage(Orderable):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='medical_image')

    panels = [
        FieldPanel('image'),
    ]

    class Meta:
        db_table = 'medical_image'
'''
