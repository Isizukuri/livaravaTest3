# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20160122_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnote',
            name='text',
            field=models.TextField(verbose_name='text field'),
        ),
    ]
