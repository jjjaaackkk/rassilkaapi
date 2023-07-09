from rest_framework import serializers

from core.models import Campaign, Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('tag','tel','tmz')

    tag = serializers.CharField(max_length=100)
    tel = serializers.CharField(max_length=11)
    tmz = serializers.CharField(max_length=32)

    def create(self, data):
        return Customer.objects.create(**data)
    
    def update(self, obj, updated):
        obj.tag = updated.get('tag', obj.tag)
        obj.tel = updated.get('tel', obj.tel)
        obj.tmz = updated.get('tmz', obj.tmz)
        obj.save()
        return obj
    
class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ('message', 'filter', 'start', 'stop', 'status')

    message = serializers.CharField(max_length=160)
    filter = serializers.CharField(max_length=255)
    start = serializers.DateTimeField()
    stop = serializers.DateTimeField()
    status = serializers.IntegerField(required=False)

    def create(self, data):
        return Campaign.objects.create(**data)
    
    def update(self, obj, updated):
        obj.message = updated.get('message', obj.message)
        obj.filter = updated.get('filter', obj.filter)
        obj.start = updated.get('start', obj.start)
        obj.stop = updated.get('stop', obj.stop)
        obj.status = updated.get('status', obj.status)
        obj.save()
        return obj