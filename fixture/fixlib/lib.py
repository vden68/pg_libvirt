# -*- coding: utf-8 -*-
__author__ = 'vden'

import libvirt
import time
import os
from datetime import datetime

from model.lip_domain import Lip_domain


class Lib_helper:
    def __init__(self, app):
        self.app = app


    def connection_open(app):

        try:
            conn_open_kvm = libvirt.open('qemu:///system')
            #print("conn_open_kvm")
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
                    #print(domain.name(), '=', check_domain)

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
            clone_mame= pgl_kvm.name_sourse_image+'--'+pgl_kvm.prefix+'--'+pgl_kvm.number_test_set\
                        +'--'+str(now)[5:10].replace('-','') + '--'+str(number_clone)

            check_name=app.domain_check_for_availability(check_domain='yes--'+clone_mame, conn=conn)
            number_clone = number_clone +1

        print('\n original_name=', pgl_kvm.name_sourse_image, clone_mame)
        return clone_mame


    def start_image(app, lib_domain, conn):

        dom = conn.lookupByName(lib_domain.name())

        # if the domain is not enabled we start work domain
        if lib_domain.ID() == -1:
            dom.create()
        else:
            print("\n start_image", lib_domain.name(), lib_domain.UUIDString(), lib_domain.ID(), lib_domain.IP)

        ifaces= None
        pg_time= 0
        while ifaces is None:
            try:
                ifaces= dom.interfaceAddresses(libvirt.VIR_IP_ADDR_TYPE_IPV4).values() # ['addrs'] #['vnet0']
                #print('ifaces=', ifaces)

                for addrs in ifaces:
                    print('addrs=', addrs['addrs'])
                    print()

                    for ifa in addrs['addrs']:
                        #print('ifa=', ifa['addr'])
                        lib_domain.IP = ifa['addr']
                        lib_domain.ID = dom.ID
                        print(lib_domain.IP)


            except:
                ifaces = None

            if lib_domain.IP is None:
                ifaces = None

            pg_time= pg_time+1
            time.sleep(1)
            if pg_time>200:
                print('Failed not received IP address ')
                exit(1)

        return lib_domain

    def clone_image (app, clone_name, name_image, conn):

        num = 1
        while num<60:
            try:
                os.system('virt-clone --connect qemu:///system --original %s --name %s --auto-clone' \
                     % (name_image, clone_name))
            except:
                pass

            time.sleep(2)
            check_name = app.domain_check_for_availability(check_domain=clone_name, conn=conn)
            #print('check_name = ', check_name.name())
            if check_name is not None:
                break
            num = num+1
            time.sleep(10)

    def rename_image(app, name_image, name_image_new, conn):

        dom = conn.lookupByName(name_image)

        dom.rename(name_image_new)












