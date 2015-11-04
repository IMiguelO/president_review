# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151029_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='review',
            new_name='question',
        ),
    ]
