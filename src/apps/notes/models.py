import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


def image_directory_path(instance, filename):
    """Define image upload path"""
    ext = filename.split('.')[-1]
    filename = 'path/to/save/{0}.{1}'.format(uuid.uuid4().hex, ext)
    return filename


class Book(models.Model):
    """Book model, that stores text notes"""
    title = models.CharField(
        max_length=36,
        verbose_name=_("book title")
    )

    note = models.ManyToManyField(
        'TextNote',
        blank=True,
        )

    class Meta:
        verbose_name_plural = _("books")
        app_label = 'notes'

    def __unicode__(self):
        return self.title


class TextNote(models.Model):
    """Text Notes"""
    text = models.TextField(
        verbose_name=_("text field"),
        )

    image = models.ImageField(
        upload_to=image_directory_path,
        blank=True,
        null=True,
        )

    class Meta:
        verbose_name_plural = _("text notes")
        app_label = 'notes'

    def __unicode__(self):
        return self.text

    def delete(self, *args, **kwargs):
        for book in self.book_set.all():
            if len(book.note.all()) == 1:
                book.delete()
        super(TextNote, self).delete(*args, **kwargs)
