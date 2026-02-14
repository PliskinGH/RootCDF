from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage
from django.views.generic.base import TemplateView

# Create your views here.

def home(request):
    extra_context = {}
    home_pages = FlatPage.objects.filter(url__istartswith="/home/")
    if (home_pages.count()):
        extra_context['flatpage'] = home_pages.first()
    
    return TemplateView.as_view(template_name="flatpages/default.html",
                                extra_context=extra_context)(request)