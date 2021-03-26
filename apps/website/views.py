"""
Website views
"""

from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView

from admin_panel.models.page_index import IndexPage


class IndexPage(TemplateView):
    """
    Index page views
    """
    template_name = "website/index.html"

class AboutPage(TemplateView):
    template_name = "website/about.html"


class ServicesPage(TemplateView):
    template_name = "website/services.html"


class ContactsPage(TemplateView):
    template_name = "website/contacts.html"


class LoginPage(TemplateView):
    template_name = "website/login.html"
