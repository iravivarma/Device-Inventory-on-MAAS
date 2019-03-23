from django.shortcuts import render
from django.shortcuts import render_to_response , get_object_or_404
# Create your views here.
from django.template import Context, RequestContext
from appserver.models import *
from django.http import HttpResponse
from django.db import connection

def imprt(request):
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
	info_type=request.GET.get('info_type')
#	return HttpResponse(int_type)
	data = dev_info(sys_id=sys_id,machine_name=machine_name,mac_addr=mac_addr,ram=ram,ip_addr=ip_addr,int_name=int_name,int_type=int_type,pwrstatus=pwrstatus,cpu_cores=cpu_cores,cpu_type=cpu_type,storage=storage)
	try:
		data.save()
		return HttpResponse("import done")
	except:
		return HttpResponse("import not done")
def export(request):
	machine_name=request.GET.get('machine_name')
#	return HttpResponse(machine_name)
	with connection.cursor() as cursor:
		cursor.execute("""select * from appserver_dev_info where machine_name= %s """,[machine_name] )
		row = cursor.fetchall()
		fields=cursor.description
		list=[]
		list.append([r[0] for r in fields])
		s=""
		f=[]
		r=[]
		for i in row:
			f.append(i)
		for j in range(len(f)):
			c=0
			for k in f[j]:
                		p= str(list[0][c])+":"+ str(k) + "\n" 
                		r.append(p)
                		c=c+1
	try:		
		return HttpResponse(r)
	except:
		return HttpResponse("export not done")
