import requests
import json


def send_msg(msgId, apikey, tel, text):

    url = f'https://probe.fbrq.cloud/v1/send/{msgId}'
    
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json',
        }

    data = {
        'msgId': msgId,
        'phone': tel,
        'text': text,
        }
    
    return requests.post(
        url, 
        json=data, 
        headers=headers, 
        timeout=5
        )
    
