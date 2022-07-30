from django.db import models
from jsoneditor.fields.django3_jsonfield import JSONField

# Create your models here.

class Schema(models.Model):
    app_id = models.IntegerField('Application ID', default=0)
    schema_json = models.TextField('Schhema', max_length=200, 
        help_text="Please enter the decoding schema for IOT device in JSON format")
    start_date = models.DateTimeField('Start')
    end_date = models.DateTimeField('End')
    
    
    def __str__(self):
        return f"{self.app_id}"
 
class DeviceList(models.Model):
    dev_id = models.CharField('Device ID', max_length=6)
    
    def __str__(self):
        return f"{self.dev_id}"
   

class Schema2(models.Model):
    #app_id2 = models.IntegerField('Application ID 2', default=0)
    # display values from device list model
    app_id2 = models.ForeignKey(DeviceList, on_delete=models.CASCADE)
    schema_json2 = models.TextField('Schhema 2', max_length=200, 
        help_text="Please enter the decoding schema for IOT device in JSON format")
    schema_jsonfield = JSONField(default=list)
    
    def __str__(self):
        return f"{self.app_id2}"
    
