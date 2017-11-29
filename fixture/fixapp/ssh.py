__author__ = 'vden'

import os.path
import json
from fixture.fixssh.ssh import Sshh_helper

repo = None


class Ssh_helper:

    def __init__(self, app):
        self.app = app
        self.sshh= Sshh_helper(self)


    def connection_to_the_domain_by_ssh(self, domain):


        print('\n',domain.name(), domain.UUIDString(), domain.ID(), domain.IP)
        print(self.app.pgl_ssh)
        self.sshh.do_connect(args=self.app.pgl_ssh)

        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "install_repo.json")
        print(config_file)
        with open(config_file) as f:
            repo = json.load(f)
        steps= repo["ubuntu"]["steps"]

        for step in steps:
            print('\nstep=', step)
            self.sshh.do_run(command=step)

        self.sshh.do_close()



