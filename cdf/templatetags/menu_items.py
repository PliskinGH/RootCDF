from django import template
from django.contrib.flatpages.models import FlatPage

from ..models import MenuItem

register = template.Library()

@register.simple_tag
def get_menu_items():
    return MenuItem.objects.all()

@register.simple_tag
def get_home_page():
    home_pages = FlatPage.objects.filter(url__istartswith="/home/")
    home_page = None
    if (home_pages.count()):
        home_page = home_pages.first()
    return home_page