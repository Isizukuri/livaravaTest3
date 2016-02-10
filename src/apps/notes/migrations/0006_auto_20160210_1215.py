# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='note',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
