# -*- coding: utf-8 -*-


class Settings(object):
    """
    Settings class
    """
    def __init__(self, update_time):
        self.updatetime = update_time
        self.password = "azerty"
        self.interface = "eth0"
        self.update_method = "websocket"
