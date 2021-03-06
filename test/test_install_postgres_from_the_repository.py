# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest

@pytest.allure.step('Установка Postgres из репозитория')
def test_install_postgres_from_the_repository(app):

    with pytest.allure.step('Клонирование образа %s ' % app.pgl_kvm.name_source_image):
        clone_name = app.img.clone_an_image(image=app.pgl_kvm.name_source_image, clone_name=None)

    with pytest.allure.step('Стартуем виртуальную машину %s' % clone_name):
        st_domain= app.img.start_image(name_image= clone_name)

    app.pgl_ssh.ip= st_domain.IP

    with pytest.allure.step('Устанавливаем Postgres'):
        app.sh.install_postgrespro(domain=st_domain)

    clone_name_new= 'yes--'+clone_name
    with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (clone_name, clone_name_new)):
        app.img.rename_image(name_image=clone_name, name_image_new=clone_name_new)


