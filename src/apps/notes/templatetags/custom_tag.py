from django import template
from django.utils.translation import ugettext as _

from ..models import TextNote

register = template.Library()


@register.inclusion_tag('this/_custom_tag.html')
def custom_tag(note_id):
    try:
        return {'note': TextNote.objects.get(id=note_id)}
    except TextNote.DoesNotExist:
        error_text = _('Note with id ')+str(note_id)+_(' not found.')
        return {'error_text': error_text}
