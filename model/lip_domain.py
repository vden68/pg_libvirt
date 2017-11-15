__author__ = 'vden'

class Lip_domain:

    def __init__(self, name=None, UUIDString=None, ID=None):
        self.name = name
        self.UUIDString = UUIDString
        self.ID = ID

    def __repr__(self):
        return "%s,%s,%s" % (self.name, self.UUIDString, self.ID)
