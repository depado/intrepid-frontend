# -*- coding: utf-8 -*-
from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)
app.config.from_object('config')
from app import views