# -*- coding: utf-8 -*-
__author__ = 'vden'

import libvirt

conn_open_kvm = None


class ConnectionKvm:
    def __init__(self, app):
        self.app = app

    def connection_open(app):

        global conn_open_kvm
        
        print("test")

        if conn_open_kvm is None:
            try:
                conn_open_kvm = libvirt.open('qemu:///system')
                print("Создан коннект")
            except:
                if conn_open_kvm == None:
                    print('Failed to open connection to qemu:///system')
                    exit(1)



        return conn_open_kvm




