# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20151102_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='review',
            new_name='question',
        ),
    ]
