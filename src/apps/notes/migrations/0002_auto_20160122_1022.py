# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textnote',
            options={'verbose_name_plural': 'text notes'},
        ),
        migrations.AlterField(
            model_name='textnote',
            name='text',
            field=models.CharField(max_length=256, verbose_name='text field'),
        ),
    ]
