from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib import messages

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
    """View for creating text notes wit AJAX support"""
    template_name = 'this/note_form.html'
    model = TextNote
    form_class = TextNoteForm
    message = _("Form successfully submited!")
    success_message = message

    def form_invalid(self, form):
        response = super(TextNoteCreateView, self).form_invalid(form)
        if self.request.is_ajax():
            errors = {'errors': form.errors}
            return JsonResponse(errors)
        else:
            return response

    def form_valid(self, form):
        response = super(TextNoteCreateView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': self.message,
                'notes_count': unicode(TextNote.objects.count()),
            }
            storage = messages.get_messages(self.request)
            del storage._queued_messages[0]
            json_response = JsonResponse(data)
            return json_response
        else:
            return response

    def get_success_url(self):
        return reverse('create_note')
