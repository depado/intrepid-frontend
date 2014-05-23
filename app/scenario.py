# -*- coding: utf8 -*-

import datetime


class Scenario(object):
    """
        Object storing a list of ScenarObject
        Useful to dump all the scenario in a single pickle object.
    """
    def __init__(self, name):
        self.name = name
        self.date_created = datetime.now()
        self.scenarobj = []


class ScenarObject(object):
    """ 
        An item to add in the Scenario list 
    """

    def __init__(self):
        self.target = None
        self.port = None
        self.module = None


class CustomModule(object):
    """
    Custom Module Object
    """
    def __init__(self, name, description, path):
        self.name = name
        self.description = description
        self.path = path


class Module(object):
    """
    Module Object
    """
    def __init__(self, name, preset, args):
        if preset:
            self.preset = preset
        if args:
            self.args = args
        self.name = name