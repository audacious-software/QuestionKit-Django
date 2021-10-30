# pylint: disable=no-member, line-too-long
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

import arrow

from six import python_2_unicode_compatible

from django.db import models

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

    def __str__(self):
        return self.questions + ' (' + self.date.isoformat() + ', ' + self.start_time.isoformat() + ' - ' + self.end_time.isoformat() + ')'

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

def incomplete_values(form_definition, form_response):
    incomplete = []

    for item in form_definition:
        if 'required' in item and item['required'] is True:
            key = item['key']

            if key in form_response:
                value = form_response[key]

                if value is None or len(value) == 0: # pylint: disable=len-as-condition
                    if (key in incomplete) is False:
                        incomplete.append(key)
            else:
                if (key in incomplete) is False:
                    incomplete.append(key)

    return incomplete
