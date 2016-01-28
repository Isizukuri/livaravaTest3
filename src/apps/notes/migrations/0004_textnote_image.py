# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import notes.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20160122_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='textnote',
            name='image',
            field=models.ImageField(null=True, upload_to=notes.models.image_directory_path, blank=True),
        ),
    ]
