# -*- coding: utf-8 -*-
__author__ = 'vden'


def test_creating_virtual_machine(app):
    clone_name=app.img.clone_an_image()
    print("created a clone with the name ", clone_name)
