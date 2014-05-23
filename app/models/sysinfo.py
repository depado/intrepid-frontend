# -*- coding: utf-8 -*-

# System Imports
import platform
import subprocess


class Sysinfo(object):
    """
    System Informations for the index page.
    Features : Network, Uptime, Uname, Distribution Name + Icon
    """
    def __init__(self):
        self.network = None
        self.uptime = None
        self.uname = subprocess.check_output(['uname', '-a'])  # Not necessary to reload
        self.distrib = self.init_distrib()
        self.distrib_icon = self.init_icon()
        self.update("eth0")

    @staticmethod
    def init_distrib():
        distinfo = platform.linux_distribution()
        if distinfo == ('', '', ''):
            with open('/etc/lsb-release', 'r') as fd:
                for line in fd.readlines():
                    if line.find("DISTRIB_DESCRIPTION") >= 0:
                        return line.split('"')[1]
            return "Unknown"
        else:
            return distinfo

    def init_icon(self):
        if self.distrib == "Arch Linux":
            return "/static/img/distro-arch.png"

    def update(self, interface):
        self.network = subprocess.check_output(['ifconfig', interface]).replace("\n", "<br />")
        self.uptime = subprocess.check_output(['uptime'])
