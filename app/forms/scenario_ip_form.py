# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField


class IpForm(Form):
    ipincluded = TextField('ipincluded')
    ipexcluded = TextField('ipexcluded')