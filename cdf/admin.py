from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from tinymce.widgets import TinyMCE

from .models import MenuItem

# Register your models here.

class TinyMCEAdminMixin:
    def formfield_for_dbfield(self, db_field, *args, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce-linklist')},
            ))
        return super().formfield_for_dbfield(db_field, *args, **kwargs)

class TinyMCEFlatPageAdmin(TinyMCEAdminMixin, FlatPageAdmin):
    pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
admin.site.register(MenuItem)