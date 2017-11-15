# -*- coding: utf-8 -*-
__author__ = 'vden'

import libvirt
import time
from datetime import datetime

from model.lip_domain import Lip_domain

conn_open_kvm = None


class Lib_helper:
    def __init__(self, app):
        self.app = app

    def connection_open(app):

        global conn_open_kvm

        if conn_open_kvm is None:
            try:
                conn_open_kvm = libvirt.open('qemu:///system')
                print("conn_open_kvm")
            except:
                if conn_open_kvm == None:
                    print('Failed to open connection to qemu:///system')
                    exit(1)

        return conn_open_kvm


    def domain_check_for_availability(app, check_domain=None, conn=None):

        if conn is None:
            conn=app.connection_open()

        lib_domain = None
        domains = conn.listAllDomains(0)
        if len(domains) != 0:

            for domain in domains:

                if domain.name() == check_domain:
                    lib_domain = Lip_domain(name=domain.name, UUIDString=domain.UUIDString, ID=domain.ID)
                    return lib_domain
                #else:
                #    print(domain.name(), '=', check_domain)

        else:
            print('  None')

        return lib_domain

    def domain_shutdown_name(app, conn = None, lib_name=None):
        comm = conn.lookupByName(lib_name)

        while conn.lookupByName(lib_name).ID() != -1:

            try:
                comm.shutdown()
            except:
                print('shutdown')

            time.sleep(1)

        print("domain_shutdown_name " + lib_name)

    def create_clone_name(app, pgl_kvm, conn):

        check_name = pgl_kvm.name_sourse_image
        number_clone = 0

        while check_name is not None:
            now = datetime.today()
            clone_mame= pgl_kvm.name_sourse_image+'-'+pgl_kvm.prefix+'-'+pgl_kvm.number_test_set\
                        +'-'+str(now)[5:10].replace('-','') + '-'+str(number_clone)

            check_name=app.domain_check_for_availability(check_domain=clone_mame, conn=conn)
            number_clone = number_clone +1




        print('original_name=', pgl_kvm.name_sourse_image, clone_mame)
        return clone_mame



