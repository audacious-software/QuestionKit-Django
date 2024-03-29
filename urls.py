# pylint: disable=line-too-long, no-name-in-module

import sys

from .views import schedule_json

if sys.version_info[0] > 2:
    from django.urls import re_path

    urlpatterns = [
        re_path(r'^schedule/(?P<identifier>.+).json$', schedule_json, name='question_kit_schedule_json'),
    ]
else:
    from django.conf.urls import url

    urlpatterns = [
        url(r'^schedule/(?P<identifier>.+).json$', schedule_json, name='question_kit_schedule_json'),
    ]
