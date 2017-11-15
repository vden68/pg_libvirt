# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.fixapp.clone_an_image import Clone_an_image_helper


class Application:

    def __init__(self, pgl_kvm):
        self.lib = Clone_an_image_helper(self)
        self.pgl_kvm = pgl_kvm


    def destroy(self):
        pass