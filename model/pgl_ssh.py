__author__ = 'vden'

class Pgl_ssh:

    def __init__(self, ip=None, username=None, password=None, password_root=None):
        self.ip = ip
        self.username= username
        self.password= password
        self.password_root= password_root

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.ip, self.username, self.password, self.password_root)
