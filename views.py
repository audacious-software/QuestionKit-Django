# pylint: disable=no-member

import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import QuestionSet, ScheduledItem

@csrf_exempt
def schedule_json(request, identifier): # pylint: disable=unused-argument
    seen_questions = []

    items = []

    for item in ScheduledItem.objects.filter(respondent=identifier).order_by('date', 'start_time'):
        item_dict = item.to_dict()

        items.append(item_dict)

        if (item_dict['questions'] in seen_questions) is False:
            seen_questions.append(item_dict['questions'])

    questions = {}

    for question_id in seen_questions:
        questions[question_id] = QuestionSet.objects.filter(identifier=question_id).first().to_dict()

    payload = {
        'schedule': items,
        'questions': questions
    }

    return HttpResponse(json.dumps(payload, indent=2), content_type='application/json', status=200)
