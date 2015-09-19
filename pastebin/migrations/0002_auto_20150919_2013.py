# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='syntax',
            field=models.IntegerField(default=0, choices=[(0, b'Plain'), (1, b'Python'), (2, b'HTML'), (3, b'SQL'), (4, b'Javascript'), (5, b'CSS')]),
        ),
    ]
