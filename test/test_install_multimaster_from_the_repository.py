# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest
import time

@pytest.allure.step('Установка Мультимастера из репозитория')
def test_install_multimaster_from_the_repository(app, mmts, ssh_trans):




    """
    with pytest.allure.step('Clone an image %s ' % app.pgl_kvm.name_source_image):
        clone_name = app.img.clone_an_image(image=app.pgl_kvm.name_source_image, clone_name=None)

    with pytest.allure.step('Start image %s' % clone_name):
        st_domain= app.img.start_image(name_image= clone_name)

    app.pgl_ssh.ip= st_domain.IP

    with pytest.allure.step('Install Postgres'):
        app.sh.install_postgrespro(domain=st_domain, quick_install_mode=True)

    clone_name_new= 'quick--'+clone_name
    with pytest.allure.step('Rename the virtual machine %s to %s' % (clone_name, clone_name_new)):
        app.img.rename_image(name_image=clone_name, name_image_new=clone_name_new)
    """




    clone_name_new = "quick--linux--centos--7--x86_64--pgproee--10--0608--0"
    #time.sleep(10)


    with pytest.allure.step('Clone an image %s ' % clone_name_new):
        mmts.create.clone_mmts_image(image=clone_name_new, app=app)

    with pytest.allure.step('Tuning mmts '):
        mmts.create.tuning_mmts(ssh_trans=ssh_trans)



#   sed -i '$ a \\nhost     all        all        0.0.0.0\/0       md5' /var/lib/pgpro/ent-10/data/pg_hba.conf
#   sed -i '$ a \\nhost     replication        repl        0.0.0.0\/0       trust' /var/lib/pgpro/ent-10/data/pg_hba.conf







