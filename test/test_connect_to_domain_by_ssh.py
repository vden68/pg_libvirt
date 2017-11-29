# -*- coding: utf-8 -*-
__author__ = 'vden'

def test_connect_to_domain_by_ssh(app):

    #clone_name = app.img.clone_an_image()
    clone_name = 'ubuntu1604-64-serv-tst-001-1116-0'

    st_domain= app.img.start_image(name_image= clone_name)
    print("\n st_domain= ", st_domain)
    app.pgl_ssh.ip= st_domain.IP
    print(app.pgl_ssh)
    #pgl_ssh2= app.pgl_ssh

    app.sh.connection_to_the_domain_by_ssh(domain=st_domain)
