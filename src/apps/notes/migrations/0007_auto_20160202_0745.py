# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20160202_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.ManyToManyField(related_name='notes', to='notes.TextNote', blank=True),
        ),
    ]
