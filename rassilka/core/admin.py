from django.contrib import admin
from .models import Campaign, Customer, MSG, Settings

# Register your models here.
admin.register(Campaign)(admin.ModelAdmin)
admin.register(Customer)(admin.ModelAdmin)
admin.register(MSG)(admin.ModelAdmin)
admin.register(Settings)(admin.ModelAdmin)