from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class IotappConfig(AppConfig):
    name = 'iotapp'

class Schema2AdminConfig(AdminConfig):
    default_site = 'iotapp.admin.Schema2AdminArea'
    
