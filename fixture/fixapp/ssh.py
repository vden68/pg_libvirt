__author__ = 'vden'

import os.path
import json
import pytest
from fixture.fixssh.ssh import Sshh_helper

repo = None


class Ssh_helper:

    def __init__(self, app):
        self.app = app
        self.sshh= Sshh_helper(self)


    def connection_to_the_domain_by_ssh(self, domain):

        print('\n',domain.name(), domain.UUIDString(), domain.ID(), domain.IP)

        with pytest.allure.step('Подключаемся по SSH к %s  IP адрес %s' %(domain.name(), domain.IP)):
            self.sshh.do_connect(args=self.app.pgl_ssh)

        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__))+self.app.pgl_kvm.path_meta_json)
        print(config_file)

        with pytest.allure.step('Считываем файл (json) %s' % config_file):
            with open(config_file) as f:
                repo = json.load(f)


        split_name= self.app.pgl_kvm.name_sourse_image.split('-')

        steps_system= repo[split_name[0]][split_name[1]][split_name[2]][split_name[3]]


        for steps_f in steps_system:
            steps = steps_f['install']

            with pytest.allure.step('Выполняем install из meta.json' ):
                for step in steps:
                    print('\nstep=', step)
                    with pytest.allure.step('step= sudo sh -c %s' % step):
                        self.sshh.do_run(command="sudo sh -c '"+step+"'")

        with pytest.allure.step('Выключаем ВМ'):
            self.sshh.do_run(command="sudo shutdown -h now")

                


        self.sshh.do_close()



