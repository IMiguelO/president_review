# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151030_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Jeb Bush'), (2, b'Ben Carson'), (3, b'Hillary Clinton'), (4, b'Ted Cruz'), (5, b'Lawrence Lessig'), (6, b'Martin OMalley'), (7, b'Marco Rubio'), (8, b'Bernie Sanders'), (9, b'Donald Trump'), (10, b'Guido Lang')]),
        ),
    ]
