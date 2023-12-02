from django import template

register = template.Library()

@register.filter
def decode_utf8(value):
    try:
        return value.decode('utf-8')
    except UnicodeDecodeError:
        return value