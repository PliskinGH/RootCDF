from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = "cdf"

urlpatterns = [
    path("", TemplateView.as_view(template_name="cdf/base.html"), name='home'),
]