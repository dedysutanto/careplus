from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, PermissionHelper, EditView, CreateView)
from .models import BPJSCodes


class BPJSCodesAdmin(ModelAdmin):
    model = BPJSCodes
    base_url_path = 'bpjscode'  # customise the URL from default to admin/bookadmin
    menu_label = 'BPJS Codes'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    menu_order = 90  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = [
        'code', 'description',
    ]
    search_fields = [
        'code', 'description',
    ]
    ordering = ['code']


modeladmin_register(BPJSCodesAdmin)
