# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', django_hstore.fields.DictionaryField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
