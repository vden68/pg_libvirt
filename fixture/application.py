# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.second.connection_kvm import ConnectionKvm


class Application:

    def __init__(self):
        self.conn_kvm = ConnectionKvm(self)




    def destroy(self):
        pass