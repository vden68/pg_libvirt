__author__ = 'vden'

class Lip_domain:

    def __init__(self, name=None, UUIDString=None, ID=None, IP=None):
        self.name = name
        self.UUIDString = UUIDString
        self.ID = ID
        self.IP = IP

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.name, self.UUIDString, self.ID, self.IP)
