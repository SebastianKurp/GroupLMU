from django import template
from ..models import note

register = template.Library()

@register.filter(name='get_note_contents')
def get_note_contents(value):
    return value[:10]