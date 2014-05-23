# -*- coding: utf-8 -*-

# System Imports
from psutil import cpu_percent, virtual_memory, disk_usage
import re

# Flask Imports
from flask import flash


def get_cpu_load():
    """ Returns the CPU Load """
    load = cpu_percent(interval=0, percpu=False)
    return load


def get_vmem():
    """ Returns the Ram percentage """
    mem = virtual_memory().percent
    return mem


def get_disk_usage():
    """ Returns the Disk usage """
    disk = disk_usage('/').percent
    return disk


def check_ip_string(ip):
    """ Validates if this is an IP Adress with a mask or not """
    if ip == "localhost":
        return True
    slashes = len(re.findall("/", ip))
    if slashes > 1:
        flash("Too many slashes")
        return False
        
    if slashes == 1:
        temp = ip.split("/")
        ip = temp[0]
        mask = temp[1]
        if re.search("^[1-32]", mask):
            pass
        else:
            flash("Invalid Mask")
            return False

    if re.search("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
        return True
    else:
        flash("Invalid IP")
        return False


def extension_ok(nomfic):
    """ Renvoie True si le fichier possède une extension d'image valide. """
    return '.' in nomfic and nomfic.rsplit('.', 1)[1] == 'xml'
