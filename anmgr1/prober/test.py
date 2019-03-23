#!/usr/bin/python3

from __future__ import print_function
from maas.client import login
from maas.client.enum import NodeStatus
from maas.client.utils.async import asynchronous
import MySQLdb as my
import time


client = login(
    "http://194.47.151.120:5240/MAAS/",
     username = "ats", password="atslabb00",
)
db = my.connect(host='127.0.0.1', port=3306, db='anm', user='root',passwd='root', charset='utf8mb4')
cursor = db.cursor()

a=[]; b=[]; c=[]; 
for machine in client.machines.list():
        if machine.status==NodeStatus.DEPLOYED:
           t = time.ctime()
        a.append(machine.system_id)
        b.append(machine.hostname)
        c.append(machine.status)

for i in range(0,len(c)):
    if c[i]==NodeStatus.NEW:
      print(time.ctime(),"--", a[i],"--", b[i],"--", "NEW")
    elif c[i]==NodeStatus.READY:
      print(time.ctime(),"--", a[i],"--", b[i], "--", "READY")
    elif c[i]==NodeStatus.DEPLOYED:
      print(t,"--", a[i],"--", b[i], "--", "DEPLOYED")
    else:
      print(" I am Sorry")
    
    value = False
       
    sql = "SELECT * FROM appserver_maas_info;"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
           #print (row[0],"--",row[1],"--",row[2],"--",row[3],"--",row[4])
           if (row[2] == b[i]):
               value = True
    except:
       print ("Error: unable to fecth data")

    if value == True:
       continue

    x= len(a)
    i = 0
    j =0
    while i < x:
        global machine_status
        sys_id = str(a[i])
        machine_name = str(b[i])
        machine_status = "DEPLOYED"
        time_detected= t
        maas = "insert into appserver_maas_info VALUES('%i','%s','%s','%s','%s')" % \
        (j,sys_id, machine_name,machine_status,time_detected)
        i = i+1
        ++j

        cursor.execute(maas)
        db.commit()

    

#    cursor.execute (" SELECT * FROM appserver_maas_info")
#    rows = cursor.fetchall()
#    for eachRow in rows:
#        result = eachRow
#        print (result)
