# -*- coding: utf-8 -*-

# OS Imports
import json

# Local Imports
from app import sockets
from app.functions import get_cpu_load, get_disk_usage, get_vmem

@sockets.route('/_socket_system')
def socket_system(ws):
    """
    Returns the system informations, JSON Format
    CPU, RAM, and Disk Usage
    """
    while True:
        message = ws.receive()
        if message == "update":
            cpu = round(get_cpu_load())
            ram = round(get_vmem())
            disk = round(get_disk_usage())
            ws.send(json.dumps(dict(received=message, cpu=cpu, ram=ram, disk=disk)))
        else:
            ws.send(json.dumps(dict(received=message)))
