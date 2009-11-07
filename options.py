from ConfigParser import ConfigParser
import os
from praytime import PRAYTIMES

class Options(object):
    def __init__(self):
        XDG_HOME = os.environ.get("XDG_HOME")
        if not XDG_HOME:
            XDG_HOME = os.path.join(os.environ["HOME"], ".config")
        self.filename = os.path.join(XDG_HOME, "pyazan.cfg")
        defaults = {"timeout":0, "events": ",".join(PRAYTIMES), "enabled": True}
        self.options = ConfigParser(defaults)
        self.options.read(self.filename)

    def setValue(self, section, option, value):
        if not self.options.has_section(section):
            self.options.add_section(section)
        self.options.set(section, option, value)

    def getNotifications(self):
        if self.options.has_section("notification"):
            return self.options.get("notification", "events").split(",")
        return PRAYTIMES

    def getNotificationTimeout(self):
        if self.options.has_section("notification"):
            return self.options.getint("notification", "timeout")
        return 0

    def setNotificationTimeout(self, value):
        self.setValue("notification", "timeout", value)

    def setNotifications(self, events):
        self.setValue("notifications", "events", ",".join(events))

    def save(self):
        fd = open(self.filename, "w")
        self.options.write(fd)

    def enableNotifications(self, flag):
        self.setValue("notification", "enabled", flag)

    def isNotificationEnabled(self):
        if self.options.has_section("notification"):
            return self.options.getboolean("notification", "enabled")
        else:
            return True
