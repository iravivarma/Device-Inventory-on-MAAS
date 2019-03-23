from django.shortcuts import render
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from .models import *
# Create your views here.
from django.http import HttpResponse

from django.db import connection
import re

def index(request):
    return HttpResponse("Hello, world.")

# Insert API
def insert(request):
    sys_id=request.GET.get('sys_id')
    machine_name=request.GET.get('machine_name')
    mac_addr=request.GET.get('mac_addr')
    ip_addr=request.GET.get('ip_addr')
    ram=request.GET.get('ram')
    int_name=request.GET.get('int_name')
    int_type=request.GET.get('int_type')
    pwrstatus=request.GET.get('pwrstatus')
    cpu_cores=request.GET.get('cpu_cores')
    cpu_type=request.GET.get('cpu_type')
    storage=request.GET.get('storage')
    w='([a-fA-F0-9]{2}[:|\-]?){6}'
    op='^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    p = dev_info(sys_id=sys_id,machine_name=machine_name,mac_addr=mac_addr,ram=ram,ip_addr=ip_addr,int_name=int_name,int_type=int_type,pwrstatus=pwrstatus,cpu_cores=cpu_cores,cpu_type=cpu_type,storage=storage,info_type="devices")
    a= re.compile(op).search(ip_addr)
    b=re.compile(w).search(mac_addr)
    if a and b:
    
        try:    
            p.save()        
            return HttpResponse("insert success")
        except:
            return HttpResponse("insert not success")
    else:

        return HttpResponse("format may be not correct")

#Update API
def update(request):
    sys_id=request.GET.get('sys_id')
    machine_name=request.GET.get('machine_name')
    mac_addr=request.GET.get('mac_addr')
    ip_addr=request.GET.get('ip_addr')
    ram=request.GET.get('ram')
    int_name=request.GET.get('int_name')
    int_type=request.GET.get('int_type')
    pwrstatus=request.GET.get('pwrstatus')
    cpu_cores=request.GET.get('cpu_cores')
    cpu_type=request.GET.get('cpu_type')
    storage=request.GET.get('storage')
    w='([a-fA-F0-9]{2}[:|\-]?){6}'
    op='^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    a= re.compile(op).search(ip_addr)
    b=re.compile(w).search(mac_addr)
    dev="devices"
    if a and b:

        try:
            with connection.cursor() as cursor:
                cursor.execute("""update appserver_dev_info set machine_name=%s,mac_addr=%s,ip_addr=%s,ram=%s,int_name=%s,int_type=%s,pwrstatus=%s,cpu_cores=%s,cpu_type=%s,storage=%s,info_type=%s where sys_id=%s""",[machine_name,mac_addr,ip_addr,ram,int_name,int_type,pwrstatus,cpu_cores,cpu_type,storage,dev,sys_id] )        
    
            return HttpResponse("This is the update api")
        except:
            return HttpResponse("not success")
    else:
        return HttpResponse("check format")
#Delete API
def delete(request):
    machine_name=request.GET.get('machine_name')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""delete from appserver_dev_info where machine_name=%s""",[machine_name] )        
    
        return HttpResponse("This is the delete api")
    except:
        return HttpResponse("not success")



def search(request):
    
    machine_name=request.GET.get('machine_name')
    with connection.cursor() as cursor:
        cursor.execute("""select * from appserver_dev_info where machine_name= %s """,[machine_name] )        
        row = cursor.fetchall()
        columns = cursor.description
        q=[]
        q.append([x[0] for x in columns])
        s=""
        f=[]
        x=[]
        for i in row:
            f.append(i)
        for ev in range(len(f)):
            u=0
            for aall in f[ev]:
                ll= str(q[0][u])+":"+ str(aall) + "   " 
                x.append(ll)
                u=u+1
    
    
    
    
    return HttpResponse(x)
    
    
    


def callback(request):

    verification_code = request.GET.get('verification_code')
    userid = request.GET.get('userid')
    

    context = {
        'verification_code': verification_code,
        'userid': userid,
    }

    return render_to_response('appserver/callback.html', context)
