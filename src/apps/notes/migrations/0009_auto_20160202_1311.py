# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20160202_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='note',
        ),
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.ForeignKey(blank=True, to='notes.TextNote', null=True),
        ),
    ]
