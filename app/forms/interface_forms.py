# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField, BooleanField, PasswordField, SelectField
from flask.ext.wtf import Required, NumberRange, IPAddress


class LoginForm(Form):
    password = PasswordField('password', validators = [Required()])


class SettingForm(Form):
    updatetime = TextField('updatetime')
    currentpassword = PasswordField('currentpassword')
    newpassword = PasswordField('newpassword')
    confirmpassword = PasswordField('confirmpassword')
    interface = TextField('interface')



class TermForm(Form):
    command = TextField('command')
