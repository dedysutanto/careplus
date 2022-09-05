from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, PermissionHelper)
from .models import Patients, Soaps
from crum import get_current_user


class PatientsPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        return True

    def user_can_delete_obj(self, user, obj):
        return False

    def user_can_edit_obj(self, user, obj):
        return True


class SoapsPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        return True

    def user_can_delete_obj(self, user, obj):
        return False

    def user_can_edit_obj(self, user, obj):
        return True


class PatientsAdmin(ModelAdmin):
    model = Patients
    base_url_path = 'patients'  # customise the URL from default to admin/bookadmin
    menu_label = 'Patient'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('number', 'name', 'gender', 'dob', 'calculate_age', 'address')
    search_fields = ('number', 'name', 'dob')
    permission_helper_class =  PatientsPermissionHelper
    #edit_template_name = 'patient/edit.html'

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Patients.objects.filter(user=current_user)
        else:
            return Patients.objects.all()


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
    permission_helper_class = SoapsPermissionHelper

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Soaps.objects.filter(user=current_user)
        else:
            return Soaps.objects.all()


modeladmin_register(PatientsAdmin)
modeladmin_register(SoapsAdmin)
