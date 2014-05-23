# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField, BooleanField
from app.views.constants import ips


class TypeIpForm(Form):

    def __init__(self):
        self.name = TextField("Hello")
        for x, ip in enumerate(ips.includedip):
            setattr(self, "ip{}".format(x), BooleanField(ip))
