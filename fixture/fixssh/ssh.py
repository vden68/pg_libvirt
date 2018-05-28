# -*- coding: utf-8 -*-
__author__ = 'vden'

import time
import pytest

#from eventlet.timeout import Timeout
#import eventlet

from paramiko import client


class Sshh_helper:

    def __init__(self, app):
        self.app = app
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())


    def do_connect(self, args):

        ifaces = None
        pg_time = 0
        while ifaces is None:
            try:
                self.client.connect(args.ip, username=args.username, password=args.password, look_for_keys=False)
                ifaces = 1
            except:
                ifaces = None

            pg_time = pg_time + 1
            time.sleep(1)
            if pg_time > 200:
                print('Failed not received SSH connect ')
                exit(1)

        #self.client.connect(args.ip, username=args.username, password=args.password,  look_for_keys=False)


    def do_run(self, command):

        list_exec=[]

        with pytest.allure.step('Выполняем команду %s' %command):
            stdin, stdout, stderr = self.client.exec_command(command, timeout=2400)
            time.sleep(10)
            for line in stdout.read().decode('utf8').splitlines():

                print('... %s:' % (line))

                #if stderr:
                for line_stderr in stderr.read().decode('utf8').splitlines():
                    if line_stderr:
                        print('er..%s:' % (line_stderr))
                        list_exec.append(line_stderr)

                list_exec.append(line)


            """
            for line in stdout or stderr or stdin:
                print('..' + line.strip('\n'))
                #print('line', line)
                list_exec.append(line.strip('\n'))
                time.sleep(1)
            """
            

        return list_exec
        #time.sleep(1)


    def do_close(self):
        if self.client is not None:
            self.client.close()

