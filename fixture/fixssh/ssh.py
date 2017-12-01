# -*- coding: utf-8 -*-
__author__ = 'vden'

import time

from paramiko import client


class Sshh_helper:

    def __init__(self, app):
        self.app = app
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())


    def do_connect(self, args):
        self.client.connect(args.ip, username=args.username, password=args.password,  look_for_keys=False)


    def do_run(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        for line in stdout or stderr:
            print('..' + line.strip('\n'))
            #time.sleep(1)


    def do_close(self):
        self.client.close()

