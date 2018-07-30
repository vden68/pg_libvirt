# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.fixapp.image import Image_helper
from fixture.fixapp.ssh import Ssh_helper
from fixture.fixapp.j_son import Json_helper
from fixture.fixapp.j_enkins import Jenkins_helper


class Application:

    def __init__(self, pgl_kvm, pgl_ssh, clone_name_list):
        self.img = Image_helper(self)
        self.sh= Ssh_helper(self)
        self.jsn= Json_helper(self)
        self.jnk= Jenkins_helper(self)

        self.pgl_kvm= pgl_kvm
        self.pgl_ssh= pgl_ssh

        self.clone_name_list=clone_name_list


    def destroy(self):
        print("clone_name_list=", self.clone_name_list)
        self.img.destroy_images(self.clone_name_list)