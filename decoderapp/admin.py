from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Decoder, DeviceList

from jsoneditor.fields.django3_jsonfield import JSONField
from jsoneditor.forms import JSONEditor

#to disable nav sidebar css added by django 3.1
admin.autodiscover()
admin.site.enable_nav_sidebar = False

# Register your models here.


class DecoderAdmin(admin.ModelAdmin):
 
    class Media:
        css = {
            'all': ('decoderapp/decoder_css.css',),
        }   
 
    fieldsets = (
        ("Device ID",{
            "fields": (
                'dev_id2', 
            ),
            "classes": ('stack_labels',)
            }),
            
        ("JSON Text",{
            "fields": (
                'schema_jsonfield',
            ),
            "classes": ('stack_labels',)
            }),
        ("Date Range",{
            "fields": (
                ('start_date', 'end_date',),
            ),
            "classes": ('stack_labels',)
            }),
       
        )
  
    list_display = ("dev_id2", "start_date", "end_date")
    formfield_overrides = {
        JSONField:{ 'widget':JSONEditor },
    
    }
    
     
admin.site.register(Decoder, DecoderAdmin)

class DeviceAdmin(admin.ModelAdmin):
 
    fieldsets = [
        ('Device ID', {'fields': ['dev_id']}),
        ('Owner', {'fields': ['owner']}),
        ]

    list_display = ("dev_id","owner")
    

admin.site.register(DeviceList, DeviceAdmin)

