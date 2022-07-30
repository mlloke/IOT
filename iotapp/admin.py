from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Schema, Schema2, DeviceList

from jsoneditor.fields.django3_jsonfield import JSONField
from jsoneditor.forms import JSONEditor

#to disable nav sidebar css added by django 3.1
admin.autodiscover()
admin.site.enable_nav_sidebar = False

# Register your models here.
class SchemaAdmin(admin.ModelAdmin):
    
    class Media:
        css = {
            'all': ('iotapp/custom_css1.css',),
        }
    
    """   
    fieldsets = [
        ('Application ID', {'fields': ['app_id']}),
        ('Schema', {'fields': ['schema_json']}),
        ('Date Range', {'fields': (('start_date','end_date'),)})
        ]
    """
    
    fieldsets = (
        ("Application ID",{
            "fields": (
                'app_id', 
            ),
            "classes": ('stack_labels',)
            }),
            
        ("Schema",{
            "fields": (
                'schema_json',
            ),
            "classes": ('stack_labels',)
            }),
        ("Date Range",{
            "fields": (
                ('start_date', 'end_date',),
            ),
            "classes": ('stack_labels2',)
            }),
        
        )
        

    list_display = ("app_id", "start_date", "end_date")
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':200})},
    
    }
    
    
admin.site.register(Schema, SchemaAdmin)


class SchemaAdmin2(admin.ModelAdmin):
 
    class Media:
        css = {
            'all': ('iotapp/schema2_css.css',),
        }   
    """
    fieldsets = [
        ('Application ID 2', {'fields': ['app_id2']}),
        ('Schema 2', {'fields': ['schema_json2']}),
        ]
    """

    fieldsets = (
        ("Application ID 2",{
            "fields": (
                'app_id2', 
            ),
            "classes": ('stack_labels_schema2',)
            }),
            
        ("Schema 2",{
            "fields": (
                'schema_json2',
            ),
            "classes": ('stack_labels_schema2',)
            }),
        ("Schema JSONField",{
            "fields": (
                'schema_jsonfield',
            ),
            "classes": ('stack_labels_schema2',)
            }),
       
        )
  
    list_display = ("app_id2",)
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':20})},
        JSONField:{ 'widget':JSONEditor },
    
    }
    
     
admin.site.register(Schema2, SchemaAdmin2)

class DeviceAdmin(admin.ModelAdmin):
 
    fieldsets = [
        ('Device ID', {'fields': ['dev_id']}),
        ]

    list_display = ("dev_id",)
    

admin.site.register(DeviceList, DeviceAdmin)

""" not required anymore
class Schema2AdminArea(admin.AdminSite):
    site_header = 'Schema 2 Admin Area'
    
schema2_site = Schema2AdminArea(name='Schema2Admin')

schema2_site.register(Schema2)
"""    
    