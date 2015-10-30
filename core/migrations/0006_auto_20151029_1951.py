# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151029_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='review',
        ),
    ]
