from celery import shared_task
from datetime import date, datetime
import random
import json

from .models import Campaign, Customer, MSG, Settings
from .msgapi import send_msg

def is_unique_msgId(msgId):
    try:
        MSG.objects.get(msgId=msgId)
        return False
    except MSG.DoesNotExist:
        return True
    
def genMsgId():

    a = 11995485656
    b = 99995485656

    msgid = random.randint(a, b)
    
    while not is_unique_msgId(msgid):
        msgid = random.randint(a, b)

    return msgid

@shared_task(bind=True)
def init_job(self):

    today = date.today()

    # lets filter by today
    camps = Campaign.objects.filter(
        start__year=today.year, 
        start__month=today.month, 
        start__day=today.day
        )

    if not camps.exists():
        return "nothing to do"
    
    customers = Customer.objects.all()
    
    if not customers.exists():
        return "customers empty"
    
    sets = Settings.objects.first()
    
    if not sets or not sets.api_key or sets.api_key == '':
        return "no settings"
    
    apikey = sets.api_key
    
    # camp 1 by 1
    for camp in camps:

        # check text
        text = camp.text
        
        if not text or text == '':
            continue

        start = camp.start.timestamp()
        stop = camp.stop.timestamp()
        now = datetime.now().timestamp()


        # check if time to send
        if start >= now and stop <= now and camp.status < 2:

            # set status PROCESSING
            camp.update(status=2)

            # filter customer
            filter = json.loads(camp.filter)
            
            # by operator
            if filter['operator'] and not filter['operator'] == '':
                vals = filter['operator'].split(',')
                customers = customers.filter(tel_prefix=vals)

            # by tag
            if filter['tag'] and not filter['tag'] == '':
                vals = filter['tag'].split(',')
                customers = customers.filter(tag=vals)

            if not customers.exists():
                continue
            
            # send msg 1 by 1
            for customer in customers:

                msgId = genMsgId()
                tel = int(customer.tel)

                status = send_msg(msgId, apikey, tel, text)

                message = MSG.objects.create(
                    msgId=msgId,
                    customer_id=customer.id,
                    campaign_id=camp.id,
                    status=status,
                )

                message.save()

            # set status DONE
            camp.update(status=3)

        else:
            continue

    return "done!"