from django.db import models
from django.utils.translation import ugettext_lazy as _


def image_directory_path(instance, filename):
    """Define image upload path"""
    return 'note_{0}/{1}'.format(instance, filename)


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

    class Meta:
        verbose_name_plural = _("text notes")
        app_label = 'notes'


class LastRequest(models.Model):
    """Table to store user last requests"""
    url = models.CharField(max_length=120)
    method = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{time}, url: {url}, method: {method}'.format(
            time=self.timestamp,
            url=self.url,
            method=self.method
            )
