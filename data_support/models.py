from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel


class BPJSCodes(models.Model):
    code = models.CharField(_('Code'), max_length=10)
    description = models.CharField(_('Description'), max_length=100)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    panels = [
        FieldPanel('code'), FieldPanel('description')
    ]

    class Meta:
        db_table = 'bpjs_code'
        verbose_name = 'BPJS Code'
        verbose_name_plural = 'BPJS Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)



