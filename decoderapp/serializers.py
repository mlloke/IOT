from rest_framework import serializers
from .models import DeviceList

class DeviceListSerializer(serializers.ModelSerializer):
   class Meta:
       model = DeviceList
       fields = ['dev_id', 'id']

"""
class DeviceListSerializer(serializers.Serializer):
    dev_id = serializers.CharField(max_length=6)
    
    def create(self, validated_data):
        return DeviceList.objects.create(validated_data)
        
    def update(self, instance, validated_data):
        instance.dev_id = validated_data.get('dev_id', instance.dev_id)
        instance.save()
        return instance
        
"""