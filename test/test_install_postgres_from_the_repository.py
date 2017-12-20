# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest
import time

@pytest.allure.step('Установка Postgres из репозитория')
def test_install_postgres_from_the_repository(app):

    with pytest.allure.step('Клонирование образа %s ' % app.pgl_kvm.name_sourse_image):
        clone_name = app.img.clone_an_image()

    with pytest.allure.step('Стартуем виртуальную машину %s' % clone_name):
        st_domain= app.img.start_image(name_image= clone_name)

    app.pgl_ssh.ip= st_domain.IP

    with pytest.allure.step('Устанавливаем Postgres'):
        app.sh.connection_to_the_domain_by_ssh(domain=st_domain)

    time.sleep(300)
    clone_name_new= 'yes--'+clone_name
    with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (clone_name, clone_name_new)):
        app.img.rename_image(name_image=clone_name, name_image_new=clone_name_new)


