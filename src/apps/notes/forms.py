from django.forms import ModelForm, Textarea
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator

from models import TextNote


class CustomizedField(CharField):
    """Customized CharField, that saves only uppercase chars"""
    def clean(self, value):
        if value:
            value = filter(lambda x: x.isupper(), value)
        super(CustomizedField, self).clean(value)
        return value


class TextNoteForm(ModelForm):
    """Form for adding text notes"""
    def __init__(self, *args, **kwargs):
        super(TextNoteForm, self).__init__(*args, **kwargs)
        self.fields['text'].error_messages = {'required':
                                              ('Field can not be empty and '
                                               'must contain at least 10 '
                                               'uppercase symbols!')}

    text = CustomizedField(
        validators=[MinLengthValidator(10, message=_('It must be at least 10 '
                                                     'uppercase symbols!'))],
        widget=Textarea
    )

    class Meta:
        model = TextNote
        fields = ['text']
