from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register,)
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel
from .models import Patients, Soaps
#from soap.models import Soaps, SoapRelatedLink


class PatientsAdmin(ModelAdmin):
    model = Patients
    base_url_path = 'patients'  # customise the URL from default to admin/bookadmin
    menu_label = 'Patient'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'gender', 'dob', 'calculate_age', 'address')
    #list_filter = ('',)
    search_fields = ('name', 'dob')


class SoapsAdmin(ModelAdmin):
    model = Soaps
    base_url_path = 'soaps'  # customise the URL from default to admin/bookadmin
    menu_label = 'SOAP'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('patient', 'datetime', 'soap', 'additional_info',)
    #list_filter = ('',)
    search_fields = ('patient__name',)
# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(PatientsAdmin)
modeladmin_register(SoapsAdmin)
