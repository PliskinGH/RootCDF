from django.urls import path

from . import views

app_name = "cdf"

urlpatterns = [
    path("", views.home, name='home'),
]