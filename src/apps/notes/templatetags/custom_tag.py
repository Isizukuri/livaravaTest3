from django import template

from ..models import TextNote

register = template.Library()
@register.inclusion_tag('this/_custom_tag.html')
def custom_tag(note_id):
    return{'note': TextNote.objects.get(id=note_id)}
