# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20160215_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'Изображения', 'verbose_name': 'Изображние'},
        ),
    ]
