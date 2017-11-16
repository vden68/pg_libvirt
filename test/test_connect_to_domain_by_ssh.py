# -*- coding: utf-8 -*-
__author__ = 'vden'

def test_connect_to_domain_by_ssh(app):

    #clone_name = app.img.clone_an_image()
    clone_name = 'ubuntu1604-64-serv-tst-001-1116-1'

    app.img.start_image(name_image = clone_name)
