# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='review',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
    ]
