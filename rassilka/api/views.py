from rest_framework import status as STATUS
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi

from .serializers import (
    CampaignSerializer, CustomerSerializer
)
from core.models import (
    Campaign, Customer, MSG
)
from core.stats import (
    get_stats_from_camps, get_stats_from_msgs
)
from .specs import (
    campaign_par, campaign_post_request, campaign_post_responses, campaign_get_response_all, campaign_get_response, campaign_put_request, campaign_put_responses, customer_par, customer_post_request, customer_post_responses, customer_get_response_all, customer_get_response, customer_put_responses, msg_par, stats_get_response_main, stats_get_response
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
    
def id_not_found(msg):
    content = { 'error': msg }
    return Response(content, status=STATUS.HTTP_404_NOT_FOUND)

class CustomerAPI1(APIView):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(responses=customer_get_response_all, 
                         operation_description='Запросить список рассылок'
                         )
    def get(self, req):
        return Response({
            'customers': Customer.objects.all().values()
            })
    
    @swagger_auto_schema(request_body=customer_post_request, 
                         responses=customer_post_responses,
                         operation_description='Добавление нового клиента для рассылки' 
                         )
    def post(self, req):
        serializer = CustomerSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()


class CustomerAPI2(APIView): 

    permission_classes = (IsAuthenticated, )



    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None

    @swagger_auto_schema(responses=customer_get_response, 
                         operation_description='Запросить клиента по ID'
                         )
    
    def get(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Клиент не найден!')

        return Response({
            'id': obj.id,
            'tag': obj.tag,
            'tel':  obj.tel,
            'tmz': obj.tmz,
            })
    
    @swagger_auto_schema(responses=customer_put_responses, 
                         operation_description='Внести изменения в рассылку',
                         manual_parameters=[customer_par],
                         )
    def put(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Клиент не найден!')

        serializer = CustomerSerializer(instance=obj, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    @swagger_auto_schema(responses=customer_post_responses,
                         operation_description='Удалить клиента по ID',
                         manual_parameters=[customer_par],
                         )
    def delete(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Клиент не найден!')

        obj.delete()
        return json_response()
    

class CampaignAPI1(APIView): 

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(responses=campaign_get_response_all, 
                         operation_description='Запросить список рассылок'
                         )
    def get(self, req):
        return Response({
            'campaigns': Campaign.objects.all().values()
            })

    @swagger_auto_schema(request_body=campaign_post_request, 
                         responses=campaign_post_responses,
                         operation_description='Создание новой рассылки' 
                         )
    def post(self, req):
        serializer = CampaignSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    

class CampaignAPI2(APIView): 

    permission_classes = (IsAuthenticated, )
    
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return None

    @swagger_auto_schema(responses=campaign_get_response, 
                         operation_description='Запросить рассылку по ID'
                         )
    def get(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Рассылка не найдена!')

        return Response({
            'id': obj.id,
            'message': obj.message,
            'filter':  obj.filter,
            'start': obj.start,
            'stop': obj.stop,
            'status': obj.status
            })
    
    @swagger_auto_schema(request_body=campaign_put_request,
                         responses=campaign_put_responses, 
                         operation_description='Внести изменения в рассылку', 
                         manual_parameters=[campaign_par]
                         )
    def put(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Рассылка не найдена!')

        serializer = CampaignSerializer(instance=obj, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return json_response()
    
    @swagger_auto_schema(responses=campaign_put_responses,
                         operation_description='Удалить рассылку по ID',
                         manual_parameters=[campaign_par],
                         )
    def delete(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return id_not_found('Рассылка не найдена!')

        obj.delete()
        return json_response()


class MessageAPI(APIView): 

    permission_classes = (IsAuthenticated, )
    
    def get_object(self, pk):
        try:
            return MSG.objects.get(pk=pk)
        except MSG.DoesNotExist:
            return None

    @swagger_auto_schema(responses=campaign_post_responses,
                         operation_description='Удалить сообщение по ID',
                         manual_parameters=[msg_par],
                         )
    
    def delete(self, req, pk):
        obj = self.get_object(pk)

        if not obj:
            return json_response('Сообщение не найдено!', 0)

        obj.delete()
        return json_response()
    

class StatsAPI1(APIView):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(responses=stats_get_response_main,
                         operation_description='Статистику по рассылкам',
                         )
    def get(self, req):

        result = {}
        
        camps = Campaign.objects.all()
        camp_stats = get_stats_from_camps(camps)
        result['campaigns'] = camp_stats

        msgs = MSG.objects.all()
        msg_stats = get_stats_from_msgs(msgs)
        result['messages'] = msg_stats

        return Response(result)
    

class StatsAPI2(APIView):

    permission_classes = (IsAuthenticated, )
    
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return None

    @swagger_auto_schema(responses=stats_get_response,
                         operation_description='Запросить статистику по ID рассылки',
                         manual_parameters=[campaign_par],
                         )
    
    def get(self, req, pk):

        camp = self.get_object(pk)

        if not camp:
            return id_not_found('Рассылка не найдена!')

        status = ''

        if camp.status == 1:
            status = 'новые'
        if camp.status == 2:
            status = 'запущенные'
        elif camp.status == 3:
            status = 'завершенные'
                
        succeed = 0
        failed = 0

        msgs = MSG.objects.filter(campaign_id=pk)

        if msgs:
            
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
    