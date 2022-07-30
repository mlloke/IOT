from django.db import models

from jsoneditor.fields.django3_jsonfield import JSONField

# Create your models here.

class DeviceList(models.Model):
    dev_id = models.CharField('Device ID', max_length=6)
    
    def __str__(self):
        return f"{self.dev_id}"
   

class Decoder(models.Model):
    dev_id2 = models.ForeignKey(DeviceList, on_delete=models.CASCADE)
    schema_jsonfield = JSONField(default=list)
    start_date = models.DateTimeField('Start')
    end_date = models.DateTimeField('End')
    
    def __str__(self):
        return f"{self.dev_id2}"
    

