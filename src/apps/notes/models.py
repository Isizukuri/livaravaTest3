from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator


class TextNote(models.Model):
    """Text Notes"""
    def __unicode__(self):
        return self.text

    text = models.TextField(
        verbose_name=_("text field"),
        validators=[MinLengthValidator(
                        10,
                        message=_('Can`t be shorter then 10 symbols.'))
                    ]
        )

    class Meta:
        verbose_name_plural = _("text notes")
        app_label = 'notes'
