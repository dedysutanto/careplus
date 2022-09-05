from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, )
from .models import Invoices
from crum import get_current_user


class InvoicesAdmin(ModelAdmin):
    model = Invoices
    base_url_path = 'invoices'  # customise the URL from default to admin/bookadmin
    menu_label = 'Invoice'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('patient', 'datetime', 'calculate_total')
    search_fields = ('patient__name', 'dob')

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Invoices.objects.filter(user=current_user)
        else:
            return Invoices.objects.all()


modeladmin_register(InvoicesAdmin)
