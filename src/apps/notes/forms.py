from django.forms import ModelForm

from models import TextNote

class TextNoteForm(ModelForm):
    class Meta:
        model = TextNote
        fields = ['text']
