# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.fixapp.image import Image_helper
from fixture.fixapp.ssh import Ssh_helper


class Application:

    def __init__(self, pgl_kvm, pgl_ssh):
        self.img = Image_helper(self)
        self.sh= Ssh_helper(self)

        self.pgl_kvm= pgl_kvm
        self.pgl_ssh= pgl_ssh


    def destroy(self):
        pass