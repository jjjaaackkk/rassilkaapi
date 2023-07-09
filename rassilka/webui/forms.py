from django import forms

class CampaignForm(forms.Form):
    message = forms.CharField(label="message", max_length=160)
    filter = forms.CharField(label="filter", max_length=255)
    start = forms.DateTimeField(label="start")
    stop = forms.DateTimeField(label="stop")
    status = forms.IntegerField(label="status")

class CustomerForm(forms.Form):
    tag = forms.CharField(label="tag", max_length=100)
    tel = forms.CharField(label="tel", max_length=12)
    tmz = forms.CharField(label="tmz")