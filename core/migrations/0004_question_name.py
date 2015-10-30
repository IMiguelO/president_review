# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_question_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.TextField(null=True, blank=True),
        ),
    ]
