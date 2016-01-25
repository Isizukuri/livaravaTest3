from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse

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
    form_class = TextNoteForm
    success_message = "Form successfully submited!"

    def get_success_url(self):
        return reverse('create_note')
