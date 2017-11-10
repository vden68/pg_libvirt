# -*- coding: utf-8 -*-
__author__ = 'vden'
from fixture.fixlib.lib import Lib_helper

class Clone_an_image_helper:
    def __init__(self, app):
        self.app = app
        self.flib = Lib_helper(self)


    def clone_an_image(self):
        print("\n Hello")
        conn_open_kvm = self.flib.connection_open()