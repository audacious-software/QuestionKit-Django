# -*- coding: utf-8 -*-
# pylint: skip-file

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=512, unique=True)),
                ('name', models.CharField(max_length=1024)),
                ('definition', models.TextField(max_length=4194304)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=512)),
                ('item_start', models.DateTimeField()),
                ('item_end', models.DateTimeField(blank=True, null=True)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_items', to='question_kit.QuestionSet')),
            ],
        ),
    ]
