import subprocess
devices=[
    {"host_name":"R1", "ip":"127.0.0.1","vendor":"Cisco"},
    {"host_name":"R2", "ip":"192.168.1.1","vendor":"Cisco"},
    {"host_name":"FW1", "ip":"8.8.8.8","vendor":"Palo Alto"},
    {"host_name":"S1", "ip":"192.168.4.1","vendor":"Cisco"},
    {"host_name":"R1", "ip":"192.168.4.2","vendor":"Cisco"},
    {"host_name":"Ex-SW1", "ip":"192.168.1.50","vendor":"Juniper"},
    {"host_name":"SRX-GW", "ip":"192.168.1.254","vendor":"Juniper"},
    ]
cisco_count=0
palo_alto_count=0
juniper_count=0
reachable_device=0
non_reachable_device=0
for device in devices:
    result=subprocess.run(
        ["ping","-n","1",device["ip"]],
        capture_output=True,
        text=True
        )
    if result.returncode==0:
        print(f'the reachable devices ip :{device["ip"]}')
        reachable_device+=1
    else:
        print(f'the non reachable devices ip :{device["ip"]}')
        non_reachable_device+=1
    
    if device["vendor"]=="Cisco":
        cisco_count+=1
        
    elif device["vendor"]=="Juniper" :
        juniper_count+=1
        
    else:
        palo_alto_count+=1
        

print(" Total devices are :",len(devices))
print(f" Total Cisco devices :{cisco_count}")
print(f" Total palo alto  devices :{palo_alto_count}")
print(f" Total Juniper devices :{juniper_count}")
print(f" up devices :{reachable_device}")
print(f" down devices :{non_reachable_device}")
        
