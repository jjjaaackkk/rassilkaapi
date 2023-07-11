from django.test import TestCase
from .msgapi import send_msg
from .models import Settings

# API test
print('probe.fbrq.cloud api test')
sets = Settings.objects.first()

test_obj = {
    'params': [],
    'id': 11995475656,
    'apikey': sets.api_key,
    'tel': int('79225667888'),
    'msg': 'test',
    'status_code': 0,
    'result': '',
}

test_obj['params'] = [test_obj['id'], test_obj['apikey'], test_obj['tel'], test_obj['msg']]

r = send_msg(
    test_obj['id'], test_obj['apikey'], test_obj['tel'], test_obj['msg']
    )

test_obj['status_code'] = r.status_code
test_obj['result'] = r.text

print(test_obj)
