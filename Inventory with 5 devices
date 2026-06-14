devices=[
    {"host_name":"R1", "ip":"192.168.1.1","vendor":"cisco","status":"up"},
    {"host_name":"S1", "ip":"192.168.1.2","vendor":"cisco","status":"up"},
    {"host_name":"FW1", "ip":"192.168.1.3","vendor":"palo alto","status":"down"},
    {"host_name":"R2", "ip":"10.0.0.1","vendor":"cisco","status":"down"},
    {"host_name":"S2", "ip":"10.0.0.2","vendor":"cisco","status":"down"}
    ]
count=0
print(len(devices))# = 5 total devices are 5
for device in devices:
    if device["vendor"]=="cisco":
        count+=1 #= 4 total cisco devices 4
    if device["status"]=="up":
        count+=1 #= 2 total 2 devices has up status
    if device["status"]=="down":
        count+=1 #=3 total 3 devices has down status
    if device["vendor"]=="cisco":
        print(f'{device["host_name"]}')#= R1,S1,R2,S2 are the  Cisco devices 
    if device["ip"].startswith("192.168"):
        print(f'{device["host_name"]}')# =R1,S1 and FW1 are the devices  starts with 192.168 ip address       
print(count)
