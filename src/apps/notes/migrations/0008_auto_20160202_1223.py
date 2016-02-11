# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20160202_0745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'books'},
        ),
        migrations.RemoveField(
            model_name='textnote',
            name='book',
        ),
        migrations.AlterField(
            model_name='book',
            name='note',
            field=models.ManyToManyField(to='notes.TextNote', blank=True),
        ),
    ]
