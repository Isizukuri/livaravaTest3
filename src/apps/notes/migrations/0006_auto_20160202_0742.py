# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20160201_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.ManyToManyField(related_name='books', to='notes.TextNote', blank=True),
        ),
        migrations.AlterField(
            model_name='textnote',
            name='book',
            field=models.ManyToManyField(to='notes.Book', blank=True),
        ),
    ]
