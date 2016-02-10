# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_textnote_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=36, verbose_name='book title')),
                ('note', models.ManyToManyField(to='notes.TextNote', blank=True)),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
    ]
