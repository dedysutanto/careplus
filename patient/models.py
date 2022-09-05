from django.db import models
from django.contrib.auth.models import User
from modelcluster.models import ClusterableModel
from django.utils.translation import gettext as _
from wagtail.models import Orderable, Page
from modelcluster.fields import ParentalKey
from django.utils.timezone import now
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, HelpPanel
from crum import get_current_user
from wagtail.admin import widgets
from datetime import date

SOAP = """S:
O:
A:
P:"""


HELP_PANEL = 'AA=BAttery; GR=GEdhe Rasa; CC=Cicak'

GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]

TEETH = [
    (None, '--'),
    ('AA', 'AA'),
    ('GR', 'GR')
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


class Patients(ClusterableModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    gender = models.CharField(max_length=3, verbose_name=_('Gender'), choices=GENDER, default='M')
    dob = models.DateField(verbose_name=_('Date of Birth'))
    address = models.TextField(verbose_name=_('Address'), blank=True, null=True)
    phone = models.CharField(max_length=50, verbose_name='Telephone/HP', blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    date_widget = widgets.AdminDateInput(
        attrs={
            'placeholder': 'yyyy-mm-dd'
        }
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([FieldPanel('name'), FieldPanel('gender')]),
            FieldPanel('dob', widget=date_widget),
            FieldRowPanel([FieldPanel('phone'), FieldPanel('email')]),
            FieldPanel('address')],
            heading='Data Patient'
        ),

        MultiFieldPanel([
            HelpPanel(content=HELP_PANEL,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            InlinePanel('teeth_upper_right', heading='Upper Right', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
            InlinePanel('teeth_upper_left', heading='Upper Left', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
        ], heading='Upper Teeth Condition', classname="collapsed"),
        MultiFieldPanel([
            HelpPanel(content=HELP_PANEL,
                      template='wagtailadmin/panels/help_panel.html', heading='', classname=''),
            InlinePanel('teeth_lower_right', heading='Lower Right', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
            InlinePanel('teeth_lower_left', heading='Lower Left', label='Condition',
                        classname="collapsed",
                        min_num=0, max_num=1),
        ], heading='Lower Teeth Condition', classname="collapsed"),
        InlinePanel('related_patient', heading="Related SOAP", label='Detail SOAP',
                    classname="collapsed",
                    min_num=None, max_num=None),
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
        return super(Patients, self).save()

    def calculate_age(self):
        today = date.today()
        try:
            age = (today.year - self.dob.year) \
                  - ((today.month, today.day) < (self.dob.month, self.dob.day))
        except ValueError:
            age = 0
        return '%d' % age

    calculate_age.short_description = _('Age')


class Soaps(Orderable):
    datetime = models.DateTimeField('Date Time', default=now)
    soap = models.TextField(verbose_name=_('SOAP'), blank=True, null=True, default=SOAP)
    additional_info = models.TextField(verbose_name=_('Additional Information'), blank=True, null=True)
    patient = ParentalKey('Patients', on_delete=models.CASCADE, related_name='related_patient')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    panels = [
        FieldRowPanel([FieldPanel('patient'), FieldPanel('datetime')]),
        FieldPanel('soap'),
        FieldPanel('additional_info'),
    ]

    class Meta:
        db_table = 'soaps'
        verbose_name = 'SOAP'
        verbose_name_plural = 'SOAP'
        ordering = ['-datetime']

    def save(self):
        if self.user is None:
            self.user = get_current_user()

        return super(Soaps, self).save()


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
