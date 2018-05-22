# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest

@pytest.allure.step('Установка Мультимастера из репозитория')
def test_install_multimaster_from_the_repository(app):

    with pytest.allure.step('Клонирование образа %s ' % app.pgl_kvm.name_source_image):
        clone_name = app.img.clone_an_image(image=app.pgl_kvm.name_source_image, clone_name=None)

    with pytest.allure.step('Стартуем виртуальную машину %s' % clone_name):
        st_domain= app.img.start_image(name_image= clone_name)

    app.pgl_ssh.ip= st_domain.IP

    with pytest.allure.step('Устанавливаем Postgres'):
        app.sh.install_postgrespro(domain=st_domain,  quick_install_mode=True)

    with pytest.allure.step('Создаем ноды на основе  %s' % clone_name):
        app.img.creating_nodes(clone_name=clone_name)



#   sed -i '$ a \\nhost     all        all        0.0.0.0\/0       md5' /var/lib/pgpro/ent-10/data/pg_hba.conf
#   sed -i '$ a \\nhost     replication        repl        0.0.0.0\/0       trust' /var/lib/pgpro/ent-10/data/pg_hba.conf







