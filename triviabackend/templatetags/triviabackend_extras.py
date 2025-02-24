from django import template
from random import randrange

register = template.Library()

@register.filter("increment")
def increment(value, arg=1):
    return value + arg