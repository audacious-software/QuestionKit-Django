# -*- coding: utf-8 -*-
# pylint: disable=no-member

from __future__ import unicode_literals

import json

from django.db import models

class QuestionSet(models.Model):
    identifier = models.CharField(max_length=512, unique=True)
    name = models.CharField(max_length=1024)

    definition = models.TextField(max_length=4194304)

    def __unicode__(self):
        return self.name + ' (' + self.identifier + ')'

    def to_dict(self):
        dict_obj = {
            'id': self.identifier,
            'name': self.name,
            'definition': json.loads(self.definition)
        }

        return dict_obj

class ScheduledItem(models.Model):
    respondent = models.CharField(max_length=512)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    questions = models.ForeignKey(QuestionSet, related_name='scheduled_items')

    def to_dict(self, id_prefix=''):
        dict_obj = {
            'id': id_prefix + str(self.pk),
            'respondent': self.respondent,
            'date': self.date.isoformat(),
            'start': self.start_time.isoformat(),
            'end': self.end_time.isoformat(),
            'questions': self.questions.identifier,
        }

        return dict_obj
