# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151029_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
