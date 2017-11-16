# -*- coding: utf-8 -*-
__author__ = 'vden'

from fixture.fixapp.image import Image_helper


class Application:

    def __init__(self, pgl_kvm):
        self.img = Image_helper(self)
        self.pgl_kvm = pgl_kvm


    def destroy(self):
        pass