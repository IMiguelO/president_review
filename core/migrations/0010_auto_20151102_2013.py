# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151102_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='review',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='email',
        ),
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
