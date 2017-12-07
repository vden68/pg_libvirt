# -*- coding: utf-8 -*-
__author__ = 'vden'

import allure

@allure.step('проверка')
def test_connect_to_domain_by_ssh(app):

    with allure.step('Проверка шага clone_name={clone_name}'):
        clone_name = app.img.clone_an_image()
    #clone_name = 'ubuntu1604-64-serv-tst-001-1116-0'
    #clone_name = 'centos6-pg96'
    #clone_name='linux-ubuntu-16.04-x86_64'

    st_domain= app.img.start_image(name_image= clone_name)
    print("\n st_domain= ", st_domain)
    app.pgl_ssh.ip= st_domain.IP
    print(app.pgl_ssh)

    app.sh.connection_to_the_domain_by_ssh(domain=st_domain)
