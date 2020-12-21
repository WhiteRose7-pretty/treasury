from django import template

register = template.Library()


@register.simple_tag
def string_float(str):
    try:
        val = float(str)
    except:
        val = str
    return val
