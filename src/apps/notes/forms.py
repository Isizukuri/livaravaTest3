from django.forms import ModelForm

from models import TextNote


class TextNoteForm(ModelForm):
    """Form for adding text notes"""
    class Meta:
        model = TextNote
        fields = ['text']
