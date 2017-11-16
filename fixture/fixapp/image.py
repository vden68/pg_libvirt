# -*- coding: utf-8 -*-
__author__ = 'vden'
import os
from fixture.fixlib.lib import Lib_helper

class Image_helper:
    def __init__(self, app):
        self.app = app
        self.flib = Lib_helper(self)


    def clone_an_image(self):
        conn_open_kvm = self.flib.connection_open()

        lib_domain = self.flib.domain_check_for_availability(check_domain=self.app.pgl_kvm.name_sourse_image,
                                                             conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' %self.app.pgl_kvm.name_sourse_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        clone_name = self.flib.create_clone_name(pgl_kvm=self.app.pgl_kvm, conn=conn_open_kvm)


        os.system('virt-clone --original %s --name %s --auto-clone' % (self.app.pgl_kvm.name_sourse_image, clone_name))

        conn_open_kvm.close()

        return clone_name


    def start_image(self, name_image):

        conn_open_kvm = self.flib.connection_open()

        lib_domain = self.flib.domain_check_for_availability(check_domain=name_image,
                                                             conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' % name_image)
            exit(0)

        # if the domain is not enabled we start work domain
        if lib_domain.ID() == -1:
            self.flib.start_image(name_image=name_image, conn=conn_open_kvm)
        else:
            print("\n start_image", name_image)

        conn_open_kvm.close()

