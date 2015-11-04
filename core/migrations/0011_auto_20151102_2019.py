# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151102_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 11, 2, 20, 19, 31, 391587, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Jeb Bush'), (2, b'Ben Carson'), (3, b'Hillary Clinton'), (4, b'Ted Cruz'), (5, b'Lawrence Lessig'), (6, b'Martin OMalley'), (7, b'Marco Rubio'), (8, b'Bernie Sanders'), (9, b'Donald Trump'), (10, b'Guido Lang')]),
        ),
    ]
