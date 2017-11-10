# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.fixapp.clone_an_image import Clone_an_image_helper

#from fixture.connection_kvm import Connection_kvm_helper


class Application:

    def __init__(self):
        self.lib = Clone_an_image_helper(self)


    def destroy(self):
        pass