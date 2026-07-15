import csv
import subprocess
total_device=0
reachable_device=0
unreachable_device=0
cisco_device=0
juniper_device=0
palo_alto_device=0
arista_device=0
fortinet_device=0

with  open("network_health_monitoring.csv","r") as file:
    reader=csv.DictReader(file)

    for device in reader:
        total_device+=1
        result=subprocess.run(
            ["ping","-n","4",device['ip']],
            capture_output=True,
            text=True
            )
        if result.returncode==0:
            reachable_device+=1
            print(f' checking {device["host_name"]} - {device["ip"]} - {device["vendor"]} ---> "Up" ')
        else:
            unreachable_device+=1
            print(f' checking {device["host_name"]} - {device["ip"]} - {device["vendor"]} ---> "Down" ')
            
        if  device["vendor"]=="Cisco":
            cisco_device+=1

        elif  device["vendor"]=="Juniper":
             juniper_device+=1
            
        elif  device["vendor"]=="Palo Alto":
             palo_alto_device+=1

        elif  device["vendor"]=="Arista":
             arista_device+=1

        elif  device["vendor"]=="Fortinet":
            fortinet_device+=1


print("======================= Network health report=========")
print(" total devices : ",total_device)
print("reachable devices : " ,reachable_device)
print(" un reachable devices : " ,unreachable_device)
print("                           ")
print(" cisco devices : ", cisco_device)
print(" Juniper devices : ", juniper_device)
print(" Palo Alto devices : ", palo_alto_device)
print(" Arista devices : ", arista_device)
print(" Fortinet devices : ", fortinet_device)



