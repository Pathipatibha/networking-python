# Multi-Vendor Network Health Monitor

A lightweight Python script that automates ping sweeps and status monitoring across a multi-vendor network environment (Cisco, Juniper, Palo Alto, Arista, Fortinet). 

## How It Works
1. The script reads a list of target devices from a local `network_health_monitoring.csv` file.
2. It extracts the Hostname, IP address, and Vendor fields.
3. It utilizes the `subprocess` module to ping each device, detecting live or unreachable nodes.
4. It outputs a summary report classifying the active inventory by vendor type.

## Sample CSV Format
To run this script, your `network_health_monitoring.csv` should follow this schema:
```csv
host_name,ip,vendor
switch-core-01,192.168.1.1,Cisco
edge-firewall-01,192.168.2.1,Palo Alto
juniper-router-01,10.0.0.5,Juniper
