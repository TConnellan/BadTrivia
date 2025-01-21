from django import template

register = template.Library()

@register.filter("increment")
def increment(value, arg=1):
    return value + arg