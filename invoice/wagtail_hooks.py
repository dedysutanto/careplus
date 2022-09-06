from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, PermissionHelper)
from .models import Invoices
from crum import get_current_user


class InvoicesPermissionHelper(PermissionHelper):
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
            '''
            if obj.is_final:
                return False
            else:
                return True
            '''


class InvoicesAdmin(ModelAdmin):
    model = Invoices
    base_url_path = 'invoices'  # customise the URL from default to admin/bookadmin
    menu_label = 'Invoice'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('number', 'doctor', 'patient_number', 'datetime', 'calculate_total')
    list_filter = ('doctor',)
    search_fields = ('number', 'doctor', 'patient__name', 'dob')
    ordering = ['-number']
    permission_helper_class = InvoicesPermissionHelper

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Invoices.objects.filter(user=current_user)
        else:
            return Invoices.objects.all()


modeladmin_register(InvoicesAdmin)
