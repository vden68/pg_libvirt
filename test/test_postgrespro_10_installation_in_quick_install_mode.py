# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest

@pytest.allure.step('Postgrespro 10 installation in quick install mode')
def test_postgrespro_10_installation_in_quick_install_mode(app):

    with pytest.allure.step('Clone an image %s ' % app.pgl_kvm.name_source_image):
        clone_name = app.img.clone_an_image(image=app.pgl_kvm.name_source_image, clone_name=None)

    with pytest.allure.step('Start image %s' % clone_name):
        st_domain= app.img.start_image(name_image= clone_name)

    app.pgl_ssh.ip= st_domain.IP

    with pytest.allure.step('Install Postgres'):
        app.sh.install_postgrespro(domain=st_domain, quick_install_mode=True)

    clone_name_new= 'quick--'+clone_name
    with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (clone_name, clone_name_new)):
        app.img.rename_image(name_image=clone_name, name_image_new=clone_name_new)


