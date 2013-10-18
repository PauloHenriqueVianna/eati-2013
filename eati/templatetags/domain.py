from django import template
from django.contrib.sites.models import Site

register = template.Library()


def get_domain():
    
    return Site.objects.get_current() 

register.simple_tag(get_domain)