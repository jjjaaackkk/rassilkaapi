from django.db import models
import pytz 

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class Campaign(models.Model):

    class Meta:
        ordering = ['-id']

    message = models.CharField(max_length=160)
    filter = models.CharField(default='', max_length=255)
    start = models.DateTimeField(null=True)
    stop = models.DateTimeField(null=True)

    # 1 - ready, 2 - started, 3 - finished
    status = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    
class Customer(models.Model):

    class Meta:
        ordering = ['-id']

    tag = models.CharField(default='', max_length=100)
    tel_prefix = models.PositiveSmallIntegerField(null=True)
    tel = models.CharField(default='', max_length=12)
    tmz = models.CharField(
        max_length=32, 
        choices=TIMEZONES, 
        default='Europe/Moscow'
        )

    def __str__(self):
        return '{}'.format(self.id)
    
    def save(self, *args, **kwargs):

        if self.tel:
            self.tel_prefix = self.tel[1:4]

        super(Customer, self).save(*args, **kwargs)

class MSG(models.Model):

    class Meta:
        ordering = ['msgId']

    msgId = models.PositiveBigIntegerField(unique=True)

    customer = models.ForeignKey(
        Customer, 
        on_delete=models.SET_NULL, 
        null=True,
    )

    campaign = models.ForeignKey(
        Campaign, 
        on_delete=models.SET_NULL, 
        null=True,
    )
    
    status = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.id)
