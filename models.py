# pylint: disable=no-member, line-too-long
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

import arrow

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class QuestionSet(models.Model):
    identifier = models.CharField(max_length=512, unique=True)
    name = models.CharField(max_length=1024)

    definition = models.TextField(max_length=4194304)

    def __str__(self):
        return self.name + ' (' + self.identifier + ')'

    def to_dict(self):
        dict_obj = {
            'id': self.identifier,
            'name': self.name,
            'definition': json.loads(self.definition)
        }

        return dict_obj

@python_2_unicode_compatible
class ScheduledItem(models.Model):
    respondent = models.CharField(max_length=512)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    questions = models.ForeignKey(QuestionSet, related_name='scheduled_items', on_delete=models.CASCADE)

    def to_dict(self, id_prefix=''):
        dict_obj = {
            'id': id_prefix + str(self.pk),
            'respondent': self.respondent,
            'date': self.date.isoformat(),
            'start': self.start_time.isoformat(),
            'questions': self.questions.identifier,
        }

        if self.start_time == self.end_time:
            end_time = arrow.get(self.end_time.isoformat(), 'HH:mm:ss')
            end_time = end_time.shift(minutes=-1)

            self.end_time = end_time.datetime.time()

        dict_obj['end'] = self.end_time.isoformat()

        return dict_obj
