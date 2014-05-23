# -*- coding: utf-8 -*-

# Flask Imports
from flask import jsonify

# Local Imports
from app import app
from app.views.constants import info, globalsettings


@app.route('/_sysinfo', methods=['GET'])
def sysinfo():
    """
    Returns the global system informations, JSON Format
    Uname, Uptime, and Network
    """
    info.update(globalsettings.interface)
    return jsonify(uname=info.uname, uptime=info.uptime, net=info.network)
