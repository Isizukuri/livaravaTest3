from django.views.generic import ListView, TemplateView
from django.utils.translation import ugettext as _

from models import TextNote


class TextNoteListView(ListView):
    """View that displays list of text notes"""
    template_name = "this/index.html"
    model = TextNote


class CustomTagView(TemplateView):
    """View with custom inclusion tag demo"""
    template_name = 'this/custom_tag.html'
