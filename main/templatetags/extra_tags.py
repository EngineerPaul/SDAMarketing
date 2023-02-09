from django import template
from datetime import date


register = template.Library()


@register.simple_tag
def get_year():
    year = date.today().year
    return year
