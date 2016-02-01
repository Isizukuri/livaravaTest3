from django.db import models
from django.utils.translation import ugettext_lazy as _


def image_directory_path(instance, filename):
    """Define image upload path"""
    return 'note_{0}/{1}'.format(instance, filename)


class Book(models.Model):
    """Book model, that stores text notes"""
    def __unicode__(self):
        return self.title

    title = models.CharField(
        max_length=36,
        verbose_name=_("book title")
    )


class TextNote(models.Model):
    """Text Notes"""
    def __unicode__(self):
        return self.text

    text = models.TextField(
        verbose_name=_("text field"),
        )

    image = models.ImageField(
        upload_to=image_directory_path,
        blank=True,
        null=True,
        )

    book = models.ManyToManyField(Book)

    class Meta:
        verbose_name_plural = _("text notes")
        app_label = 'notes'
