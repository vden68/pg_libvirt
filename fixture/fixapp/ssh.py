__author__ = 'vden'

import os.path
import json
import pytest
import time
from fixture.fixssh.ssh import Sshh_helper

repo = None


class Ssh_helper:

    def __init__(self, app):
        self.app = app
        self.sshh= Sshh_helper(self)


    def conn_ssh(self, conn_ssh_l):
        self.sshh.do_connect(args=conn_ssh_l)

    def ssh_do_run(self, command=None):
        return self.sshh.do_run(command=command)

    def ssh_close(self):
        self.sshh.do_close()


    def install_postgrespro(self, domain=None, quick_install_mode=False, shutdown=True):

        print('\n',domain.name(), domain.UUIDString(), domain.ID(), domain.IP)

        with pytest.allure.step('Подключаемся по SSH к %s  IP адрес %s' %(domain.name(), domain.IP)):
            self.sshh.do_connect(args=self.app.pgl_ssh)

        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__))+self.app.pgl_kvm.path_meta_json)
        print(config_file)

        with pytest.allure.step('Считываем файл (json) %s' % config_file):
            with open(config_file) as f:
                repo = json.load(f)


        split_name= self.app.pgl_kvm.name_source_image.split('--')

        steps_system= repo[split_name[0]][split_name[1]][split_name[2]][split_name[3]]


        for steps_f in steps_system:
            steps = steps_f['install']

            if steps_f['package'][-3:].count('deb') > 0:
                self.sshh.do_run(command="while ps ax | grep -v grep | grep unattended; do sleep 1; done") #Test
                print("For ubuntu---")


            with pytest.allure.step('Выполняем install из meta.json' ):
                for step in steps:
                    print('\nstep=', step)
                    if step.find("install")>0 and step.find("postgrespro")>0 and quick_install_mode:
                        #pass
                        step2=step[:step.find("10")+2]
                        print('\nstep=', step2)
                        self.step_sudo(step2)
                        break
                    self.step_sudo(step)



        for steps_f in steps_system:
            steps = steps_f['package'][-3:]
            print(steps.count('deb'))

            #if steps.count('deb')>0:
            self.checking_installed_packages(steps)
            print(steps)

        if shutdown:
            with pytest.allure.step('Выключаем ВМ'):
                self.sshh.do_run(command="sudo shutdown +1 -h")
            time.sleep(200)

        self.sshh.do_close()

    def step_sudo(self, step):
        with pytest.allure.step('step= sudo sh -c %s ' % step):
            list_step = self.sshh.do_run(command="sudo sh -c '" + step + "'")  # sudo sh -c
            for l_step in list_step:
                with pytest.allure.step('. %s' % l_step):
                    pass

    def checking_installed_packages(self, steps):

        with pytest.allure.step('Проверка установленных %s пакетов' % steps):

            if steps.count('deb') > 0:
                list_step = self.sshh.do_run(command="dpkg --get-selections | grep postgrespro")
            elif steps.count('rpm') > 0:
                list_step = self.sshh.do_run(command="rpm -qa | grep postgrespro")
            else:
                print("Не известный тип пакета %s" % steps)

            l_server = False
            l_client = False
            l_libs = False
            for l_step in list_step:
                with pytest.allure.step('. %s' % l_step):
                    if l_step.count("server") > 0:
                        print(l_step.count("server"))
                        l_server = True
                    if l_step.count("client") > 0:
                        l_client = True
                    if l_step.count("libs") > 0:
                        l_libs = True
                    print(l_step, l_server, l_client, l_libs)
            assert l_server or l_client or l_libs



