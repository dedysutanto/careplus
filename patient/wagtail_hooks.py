from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, PermissionHelper, EditView, CreateView)
from .models import Patients, Soaps, NextAppointment
from crum import get_current_user
from config.utils import calculate_age
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now, localtime
from config.utils import time_different
from wagtail.search import index
from wagtail.admin.panels import ObjectList
from doctor.models import Doctors
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, HelpPanel
from wagtail.admin import widgets


class SoapsCreateView(CreateView):

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_instance(self):
        instance = super().get_instance()
        user = get_current_user()
        if not user.membership.is_clinic:
            doctor = Doctors.objects.get(user=user)
            instance.doctor = doctor
        return instance
        #return getattr(self, "instance", None) or self.model()

    def get_edit_handler(self):

        #if instance.patient.is_bpjs:
        #    panels = [panel for panel in Patients.panels if panel.heading != 'Invoices']
        panels = ObjectList(Soaps.panels).bind_to_model(Soaps)
        return panels


class SoapsEditView(EditView):
    page_title = 'Editing'

    def get_page_title(self):
        return 'SOAP'

    def get_page_subtitle(self):
        return '{} ({}/{})'.format(
            self.instance.patient.name,
            self.instance.patient.gender,
            calculate_age(self.instance.patient.dob)
        )

    def get_success_url(self):
        return self.edit_url


class PatientsPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        if user.is_superuser:
            return False
        else:
            return True

    def user_can_delete_obj(self, user, obj):
        return False

    def user_can_edit_obj(self, user, obj):
        if user.is_superuser:
            return False
        else:
            return True


class SoapsPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        if user.is_superuser:
            return False
        else:
            return False

    def user_can_delete_obj(self, user, obj):
        return False

    def user_can_edit_obj(self, user, obj):
        if user.is_superuser:
            return False
        else:
            return True


class SoapsAdmin(ModelAdmin):
    model = Soaps
    base_url_path = 'soaps'  # customise the URL from default to admin/bookadmin
    menu_label = 'SOAP'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    menu_order = 60  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = [
        'number', 'doctor', 'patient', 'datetime', 'subjective', 'objective',
        'assessment', 'plan', 'additional_info', 'image_thumb',
    ]
    list_filter = ('doctor',)
    search_fields = [
        'number', 'doctor__name', 'patient__name',
    ]
    ordering = ['-number']
    permission_helper_class = SoapsPermissionHelper
    edit_view_class = SoapsEditView
    create_view_class = SoapsCreateView
    form_view_extra_js = ['soap/js/edit_soap.js']

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Soaps.objects.filter(user=current_user)
        else:
            return Soaps.objects.all()

    def get_list_display(self, request):
        current_user = get_current_user()
        doctor_list_display = [
            'number', 'patient', 'datetime', 'subjective', 'objective',
            'assessment', 'plan', 'additional_info', 'image_thumb',
        ]
        if current_user.is_superuser:
            return self.list_display
        elif not current_user.membership.is_clinic:
            return doctor_list_display
        else:
            return self.list_display


class PatientsEditView(EditView):
    page_title = 'Editing'

    def get_page_title(self):
        return 'Patient'

    def get_page_subtitle(self):
        name_text = '{} ({}/{})'.format(
            self.instance,
            self.instance.gender,
            calculate_age(self.instance.dob)
        )
        try:
            next_v = NextAppointment.objects.get(patient=self.instance)

            return '{} - Next Visit: {} ({})'.format(
                    name_text,
                    localtime(next_v.datetime).strftime("%A %d %b %Y, %H:%M"),
                    time_different(next_v.datetime)
            )

        except ObjectDoesNotExist:
            return '%s' % name_text

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        instance = context['instance']
        try:
            soap = Soaps.objects.filter(patient=instance).order_by('datetime').last()
            context['soap'] = soap
        except ObjectDoesNotExist:
            context['soap'] = None

        context['add_soap'] = SoapsAdmin().url_helper.get_action_url('create')
        name_txt = str(instance.name).replace(' ', '+')
        context['list_soap'] = SoapsAdmin().url_helper.get_action_url('index') + '?q=' + name_txt
        return context

    def get_edit_handler(self):
        instance = super().get_instance()
        panels = Patients.panels
        if Soaps.objects.filter(patient=instance).count() == 0:
            panels = [panel for panel in Patients.panels if panel.heading != 'Invoices']

        panels = ObjectList(panels)

        return panels.bind_to_model(Patients)

    def get_success_url(self):
        return self.edit_url


class PatientCreateView(CreateView):

    def get_edit_handler(self):
        instance = super().get_instance()
        panels = Patients.panels

        if Soaps.objects.filter(patient=instance).count() == 0:
            panels = [panel for panel in Patients.panels if panel.heading != 'Invoices']

        panels = ObjectList(panels)

        return panels.bind_to_model(Patients)

    def get_instance(self):
        instance = super().get_instance()
        user = get_current_user()
        if not user.membership.is_clinic:
            doctor = Doctors.objects.get(user=user)
            instance.doctor = doctor
        return instance

    '''
    def bind_to_model(self, model):
        new = self.clone()
        new.model = Patients
        new.on_model_bound()
        return new
    '''


class PatientsAdmin(ModelAdmin):
    model = Patients
    base_url_path = 'patients'  # customise the URL from default to admin/bookadmin
    menu_label = 'Patient'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    menu_order = 50  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('number', 'name', 'gender', 'dob', 'calculate_age', 'phone', 'email', 'address', 'next_visit')
    search_fields = ('number', 'name', 'dob')
    permission_helper_class = PatientsPermissionHelper
    ordering = ['-number']
    edit_template_name = 'modeladmin/edit_patient.html'
    edit_view_class = PatientsEditView
    create_view_class = PatientCreateView
    form_view_extra_js = ['patient/js/patient_invoice.js', 'patient/js/patient_soap.js']

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Patients.objects.filter(user=current_user)
        else:
            return Patients.objects.all()

    def get_edit_handler(self, instance=None, request=None):
        #print(Patients.panels)
        '''
        custom_panels = []
        for pan in Patients.panels:
            try:
                print(pan.heading)
                print(pan.classname)
                if pan.heading == 'Data Patient':
                    pan.classname = 'collapsed'
            except ValueError:
                pass
            custom_panels += [pan]
        '''
        return ObjectList(Patients.panels)
        #return ObjectList(custom_panels)


modeladmin_register(PatientsAdmin)
modeladmin_register(SoapsAdmin)
