from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    CampaignSerializer, CustomerSerializer
)
from core.models import (
    Campaign, Customer, MSG
)
from core.stats import (
    get_stats_from_camps, get_stats_from_msgs
)


def json_response(msg='', succeed=1):

    if succeed == 1:
        return Response({
            'result': 'succeed',
        })
    elif succeed == 1 and not msg == '':
        return Response({
            'result': msg,
        })
    else:
        return Response({
            'result': 'failed',
            'error': msg
        })

class CustomerAPI(APIView): 

    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return json_response('id does not exists', 0)

    def post(self, req):
        serializer = CustomerSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    def put(self, req, pk):
        obj = self.get_object(pk)
        serializer = CustomerSerializer(instance=obj, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    def delete(self, req, pk):
        print('ok')
        obj = self.get_object(pk)
        obj.delete()
        return json_response()
    
class CampaignAPI(APIView): 

    permission_classes = (IsAuthenticated, )

    def get(self, req):
        return Response({
            'campaigns': Campaign.objects.all().values()
            })
    
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return json_response('нет рассылок', 0)

    def post(self, req):
        serializer = CampaignSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    def put(self, req, pk):

        print(req.data)

        obj = self.get_object(pk)
        serializer = CampaignSerializer(instance=obj, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    def delete(self, req, pk):
        obj = self.get_object(pk)
        obj.delete()
        print(obj)
        return json_response()

class StatsData(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, req):

        result = {}
        
        camps = Campaign.objects.all()
        camp_stats = get_stats_from_camps(camps)
        result['campaigns'] = camp_stats

        msgs = MSG.objects.all()
        msg_stats = get_stats_from_msgs(msgs)
        result['messages'] = msg_stats

        return Response(result)
    
class StatsDataByCampaign(APIView):

    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return json_response('нет рассылок', 0)

    def get(self, req, pk):

        camp = self.get_object(pk)

        status = ''

        if camp.status == 1:
            status = 'новые'
        if camp.status == 2:
            status = 'запущенные'
        elif camp.status == 3:
            status = 'завершенные'

        msgs = MSG.objects.filter(campaign_id=pk)

        succeed = 0
        failed = 0

        for msg in msgs:
            if msg.status == 200:
                succeed += 1
            else:
                failed += 1

        return Response({
            'campaign_id': pk,
            'status': status,
            'messages': {
                'succeed': succeed,
                'failed': failed
            }
            })