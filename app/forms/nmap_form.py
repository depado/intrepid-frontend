# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField, BooleanField, PasswordField, SelectField
from flask.ext.wtf import Required, NumberRange, IPAddress

presets = {
    'Intense Scan': 'nmap -T4 -A -v',
    'Intense Scan plus UDP': 'nmap -sS -sU -T4 -A -v',
    'Intense Scan, all TCP Ports': 'nmap -p 1-65535 -T4 -A -v',
    'Intense Scan, no Ping': 'nmap -T4 -A -v -Pn',
    'Ping Scan': 'nmap -sn',
    'Quick Scan': 'nmap -T4 -F',
    'Quick Scan Plus': 'nmap -sV -T4 -O -F --version-light',
    'Quick Traceroute': 'nmap -sn --traceroute'
}


class NmapForm(Form):
    preset = SelectField(u'Programming Language', choices=[(presets[key], key) for key in presets.keys()])
    additional_args = TextField(u'Additionnal Args')
