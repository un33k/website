from django import template
register = template.Library()

@register.filter('type')
def type(object):
    return object.__class__.__name__