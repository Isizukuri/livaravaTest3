from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin

from models import TextNote
from forms import TextNoteForm


class TextNoteListView(ListView):
    """View that displays list of text notes"""
    template_name = "this/index.html"
    model = TextNote

class CustomTagView(TemplateView):
    """View with custom inclusion tag demo"""
    template_name = 'this/custom_tag.html'

class TextNoteCreateView(SuccessMessageMixin, CreateView):
    template_name = 'this/note_form.html'
    model = TextNote
    fields = ['text']
    success_url = ('/create_note')
    success_message = "Form successfully submited!"
