from django.db import models

# Create your models here.
#import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime

class dev_info(models.Model):
    sys_id = models.CharField(max_length=15,default="Null")
    machine_name = models.CharField(max_length=40,default="Null")
    mac_addr = models.CharField(max_length=255,unique=True)
    int_name = models.CharField(max_length=20,default="Null")
    int_type = models.CharField(max_length=255,default="Null")
    pwrstatus = models.CharField(max_length=10,default="Null")
    cpu_cores = models.IntegerField()
    cpu_type = models.CharField(max_length=255,default="Null")
    ram = models.IntegerField(default=0)     
    storage = models.FloatField(default=10.7)
    ip_addr = models.GenericIPAddressField(default="0.0.0.0")
    info_type = models.CharField(max_length=100,default="devices")

class maas_info(models.Model):
    sys_id = models.CharField(max_length=15,default="Null")
    machine_name = models.CharField(max_length=40,default="Null")
    machine_status = models.CharField(max_length=40,default="Null")
    time_detected = models.CharField(max_length=30,default="Null")
