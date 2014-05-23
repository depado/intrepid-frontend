# -*- coding: utf-8 -*-

# System Imports
import os

# Local Import
from app.models import Settings, Sysinfo, Usedip


cwd = os.getcwd()
DOSSIER_UPS = os.getcwd()+"/app/ups/"
globalsettings = Settings(update_time="2000")
info = Sysinfo()
ips = Usedip()
scenario = []
