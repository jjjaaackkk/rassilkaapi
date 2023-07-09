import requests
from django.conf import settings

def send_msg(id, tel, text):

    url = 'https://probe.fbrq.cloud/v1/send/1'
    
    headers = {
        'Authorization': 'Bearer ' + settings.SEND_API_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }
    
    data = {
        'msgId': id,
        'phone': tel,
        'text': text,
        }
    
    status = requests.post(
        url, 
        data=data, 
        headers=headers, 
        timeout=3
        ).status_code
    
    return status
    
