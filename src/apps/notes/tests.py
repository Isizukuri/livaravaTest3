# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from models import TextNote
# Create your tests here.


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
         self.assertQuerysetEqual(TextNote.objects.all(),
                                 [repr(response.context['object_list'][0]),
                                  repr(response.context['object_list'][1])],
                                 ordered=False)

    def test_no_text_notes(self):
        TextNote.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'No text notes.')
