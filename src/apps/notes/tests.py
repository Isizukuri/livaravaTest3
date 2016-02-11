# -*- coding: utf-8 -*-
import json

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.test import TestCase
from django.http import HttpRequest
from django.http import JsonResponse
from django.conf import settings

from StringIO import StringIO
from PIL import Image

from models import TextNote, LastRequest
from forms import TextNoteForm
from contextprocessor import note_count_processor


class TextNoteModelTest(TestCase):
    """Test for TextNote model"""
    def test_unicode_representation(self):
        note = TextNote(text="My entry title")
        self.assertEqual(unicode(note), note.text)

    def test_verbose_name_plural(self):
        self.assertEqual(str(TextNote._meta.verbose_name_plural), "text notes")


class TestHomePage(TestCase):
    """Test for home page with list of text notes"""
    def setUp(self):
        TextNote.objects.get_or_create(
            text="Test Note for Testing")
        TextNote.objects.get_or_create(
            text="Test Note for Testing 2")
        self.client = Client()
        self.url = reverse('home')

    def test_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'this/index.html')

    def test_quesy_set(self):
        response = self.client.get(self.url)
        self.assertQuerysetEqual(
            TextNote.objects.all(),
            [
                repr(response.context['object_list'][0]),
                repr(response.context['object_list'][1])
            ],
            ordered=False
        )

    def test_no_text_notes(self):
        TextNote.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'No text notes.')


class CustomInclusionTagPageTest(TestCase):
    """Test for page with custom inclusion tag"""
    def setUp(self):
        self.client = Client()
        self.url = reverse('custom_tag')

    def test_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'this/custom_tag.html')


class CustomInclusionTagTest(TestCase):
    """Test for custom tag, that renders text note with given id"""
    def setUp(self):
        self.note = TextNote(text="Text note")
        self.note.save()
        self.id = str(self.note.id)
        self.TEMPLATE = Template("{% load custom_tag %} \
                                {% custom_tag "+self.id+" %}")

    def test_note_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(self.note.text, rendered)

    def tearDown(self):
        self.note.delete()
        self.note = None


class TextNoteCreateTest(TestCase):
    """Test for text note creation"""
    def test_valid_data(self):
        form = TextNoteForm({"text": "LOREM IPSUM"})
        self.assertTrue(form.is_valid())
        note = form.save()
        self.assertEqual(note.text, "LOREMIPSUM")

    def test_blank_data(self):
        form = TextNoteForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'text': [u'Field can not be empty and '
                                                'must contain at least 10 '
                                                'uppercase symbols!']})

    def test_only_lowercase(self):
        form = TextNoteForm({"text": "only lowercase note"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'text': [u'Field can not be empty and '
                                                'must contain at least 10 '
                                                'uppercase symbols!']})

    def test_less_then_10_uppercases(self):
        form = TextNoteForm({"text": "Less then 10 UPPERcases"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,
                         {'text': [(u'It must be at least 10 '
                                    u'uppercase symbols!')]})

    def test_less_then_10_chars(self):
        form = TextNoteForm({"text": "NINE CHARS"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,
                         {'text': [(u'It must be at least 10 '
                                    u'uppercase symbols!')]})


class ContextProcessorsTests(TestCase):
    """Test for note count context processor"""
    fixtures = ['notes_TextNote.json']

    def test_processor(self):
        """Test groups processor"""
        request = HttpRequest()
        data = note_count_processor(request)
        self.assertEqual(data['notes_count'], 7)


class AjaxedCreateNoteViewTest(TestCase):
    """Test for create note view with AJAX"""
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_note')
        self.file_obj = StringIO()
        self.image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
        self.image.save(self.file_obj, 'png')
        self.file_obj.name = 'test.png'
        self.file_obj.seek(0)

    def test_ajax_post_status(self):
        response = self.client.post(self.url,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_ajax_post_valid_data(self):
        response = self.client.post(
            self.url,
            {
                'text': 'LOREM IPSUM',
                'image': self.file_obj,
            },
            format='json', HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertTrue(isinstance(response, JsonResponse))
        succes_message = json.dumps(
            {u'message': u'Form successfully submited!', u'notes_count': u'1'}
            )
        self.assertJSONEqual(succes_message, response.content)

    def test_ajax_post_only_lowercase(self):
        response = self.client.post(
            self.url,
            {
                'text': 'lorem ipsum',
                'image': self.file_obj,
            },
            format='json', HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertTrue(isinstance(response, JsonResponse))
        error_message = json.dumps({"errors": {"text": [(
            "Field can not be empty and must contain at least "
            "10 uppercase symbols!")]}})
        self.assertJSONEqual(error_message, response.content)

    def test_ajax_post_less_then_10_uppercases(self):
        response = self.client.post(
            self.url,
            {
                'text': 'Lorem Ipsum',
                'image': self.file_obj,
            },
            format='json', HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertTrue(isinstance(response, JsonResponse))
        error_message = json.dumps(
            {"errors": {"text": ["It must be at least 10 uppercase symbols!"]}}
            )
        self.assertJSONEqual(error_message, response.content)

    def test_ajax_post_blank_file(self):
        blank_file = StringIO()
        blank_file.name = 'not_image.file'
        blank_file.seek(0)
        response = self.client.post(
            self.url,
            {
                'text': 'LOREM IPSUM',
                'image': blank_file,
            },
            format='json', HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertTrue(isinstance(response, JsonResponse))
        error_message = json.dumps(
            {"errors": {"image": ["The submitted file is empty."]}})
        self.assertJSONEqual(error_message, response.content)

    def test_ajax_post_invalid_image(self):
        not_image = StringIO()
        not_image.write('First line.\n')
        not_image.name = 'not_image.file'
        not_image.seek(0)
        response = self.client.post(
            self.url,
            {
                'text': 'LOREM IPSUM',
                'image': not_image,
            },
            format='json', HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertTrue(isinstance(response, JsonResponse))
        error_message = json.dumps(
            {'errors': {'image': [(
                    'Upload a valid image. The file you '
                    'uploaded was either not an image or '
                    'a corrupted image.')]}})
        self.assertJSONEqual(error_message, response.content)


class MiddlewareTest(TestCase):
    """Test for custom middleware"""
    def test_common_requests(self):
        self.client.get(reverse('home'))
        self.client.get(reverse('custom_tag'))
        self.client.get(reverse('last_requests'))

        self.assertEqual(LastRequest.objects.count(), 3)
        self.assertEqual(
            LastRequest.objects.first().url,
            reverse('home'),
        )
        self.assertEqual(
            LastRequest.objects.all()[1].url, reverse('custom_tag'))

    def test_excluded_requests(self):
        self.client.get(reverse('admin:jsi18n'))
        self.client.get(settings.MEDIA_URL)
        self.client.get(settings.STATIC_URL)
        self.client.get(
            reverse('last_requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(LastRequest.objects.count(), 0)


class RequestListViewTest(TestCase):
    """Test for view, that displays last 10 requests"""
    def test_status(self):
        response = self.client.get(reverse('last_requests'))
        self.assertEqual(response.status_code, 200)

    def test_queryset_with_less_then_10_entries(self):
        for i in xrange(3):
            response = self.client.get(reverse('last_requests'))
        self.assertEqual(len(response.context['object_list']), 3)
        self.assertQuerysetEqual(
            response.context['object_list'],
            map(repr, LastRequest.objects.all().order_by('-timestamp')[:10])
        )

    def test_queryset_with_more_then_10_entries(self):
        for i in xrange(25):
            response = self.client.get(reverse('last_requests'))
        self.assertEqual(len(response.context['object_list']), 10)
        self.assertQuerysetEqual(
            response.context['object_list'],
            map(repr, LastRequest.objects.all().order_by('-timestamp')[:10])
        )

    def test_ajax_respone_without_request_entries(self):
        response = self.client.get(
            reverse('last_requests'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(len(json.loads(response.content)), 1)
        message = json.dumps({u'error': u'There are no requests at all.'})
        self.assertJSONEqual(message, response.content)

    def test_ajax_response_with_10_entries(self):
        for i in xrange(10):
            self.client.get(reverse('home'))
        response = self.client.get(
            reverse('last_requests'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(len(json.loads(response.content)), 10)
