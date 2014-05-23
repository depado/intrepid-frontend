# -*- coding: utf-8 -*-

# Flask Imports
from flask import jsonify

# Local Imports
from app import app
from app.functions import get_cpu_load, get_disk_usage, get_vmem


@app.route('/_ajax_system', methods= ['GET'])
def ajax_system():
    cpu = round(get_cpu_load())
    ram = round(get_vmem())
    disk = round(get_disk_usage())
    return jsonify(cpu=cpu, ram=ram, disk=disk)