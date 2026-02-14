from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.core.validators import EMPTY_VALUES

# Create your models here.

class MenuItem(models.Model):
    """
    MenuItem, can be either an absolute URL, or a flatpage.
    """
    title = models.CharField(max_length=200, blank=True,
                             verbose_name=_('title'),
                             help_text=_("Optional if flat page."),)
    flatpage = models.OneToOneField(FlatPage, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="menu_item",
                                    verbose_name = _("flat page"),)
    url = models.URLField(blank=True, max_length=1000,
                          verbose_name="URL",
                          help_text=_("Leave blank if flat page."),)
    priority = models.IntegerField(verbose_name=_("priority"),
                                   default=0, null=False, blank=False,
                                   help_text=_("Priority of display in the menu. " \
                                   "Lower values are displayed first. " \
                                   "0 is not displayed."),)

    class Meta:
        verbose_name = _("menu item")
        verbose_name_plural = _("menu items")
        ordering = ["priority", "title"]

    def __str__(self):
        if (self.flatpage is not None):
            return self.flatpage.__str__()
        else:
            return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        if (self.flatpage is not None):
            return self.flatpage.get_absolute_url()
        elif (self.url not in EMPTY_VALUES):
            return self.url
    
    def open_in_new_context(self):
        return (self.flatpage is None and self.url not in EMPTY_VALUES)
    
    def get_title(self):
        if (self.title not in EMPTY_VALUES):
            return self.title
        elif (self.flatpage not in EMPTY_VALUES and self.flatpage.title not in EMPTY_VALUES):
            return self.flatpage.title
        else:
            return ""