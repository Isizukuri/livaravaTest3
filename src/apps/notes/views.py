import random

from django.views.generic import View, ListView, TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render

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


class WidgetGetView(TemplateView):
    """View that displays page with widget"""
    template_name = "this/widget_page.html"


class WidgetView(View):
    """View that generates widget with random text note"""
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        random_text_note = random.choice(TextNote.objects.all())
        return render(
            request,
            'this/random_widget.html',
            {"random_text_note": random_text_note}
        )
