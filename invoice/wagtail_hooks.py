from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, PermissionHelper, EditView, ButtonHelper)
from .models import Invoices
from crum import get_current_user
from django.utils.translation import gettext as _
from django.urls import reverse


class InvoicesButton(ButtonHelper):
    verbose_name = 'Print'

    send_classnames = ['button-small button-secondary']
    print_classnames = ['button-small button-secondary']

    def print_button(self, instance):
        # Define a label for our button
        text = _('Print')
        return {
            'url': reverse('print-invoice', args=(instance.number,)),
            'label': text,
            'classname': self.finalise_classname(self.print_classnames),
            'title': text,
        }

    def send_button(self, instance):

        # Define a label for our button
        text = _('Send by Email')
        return {
            'url': self.url_helper.index_url, # Modify this to get correct action
            'label': text,
            'classname': self.finalise_classname(self.send_classnames),
            'title': text,
        }

    def get_buttons_for_obj(
        self, instance, exclude=None, classnames_add=None, classnames_exclude=None
    ):
        """
        This function is used to gather all available buttons.
        We append our custom button to the btns list.
        """
        buttons = super().get_buttons_for_obj(
            instance, exclude, classnames_add, classnames_exclude
        )
        if 'print_button' not in (exclude or []):
            if instance.is_final:
                buttons.append(self.print_button(instance))

        '''
        if 'send_button' not in (exclude or []):
            if instance.is_final and instance.patient.email is not None:
                buttons.append(self.send_button(instance))
        '''
        return buttons


class InvoicesEditView(EditView):
    page_title = 'Editing'

    def get_page_title(self):
        return 'Invoice'

    def get_page_subtitle(self):
        return '%s' % self.instance.number


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
    edit_view_class = InvoicesEditView
    button_helper_class = InvoicesButton

    def get_queryset(self, request):
        current_user = get_current_user()
        if not current_user.is_superuser:
            return Invoices.objects.filter(user=current_user)
        else:
            return Invoices.objects.all()


modeladmin_register(InvoicesAdmin)
