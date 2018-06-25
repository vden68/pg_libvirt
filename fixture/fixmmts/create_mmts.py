__author__ = 'vden'

from fixture.fixapp.image import Image_helper
from model.pgl_ssh import Pgl_ssh

from fixture.fixssh.ssh import Sshh_helper
import time

class Create_mmts_helper:

    def __init__(self, mmts):
        self.img = Image_helper(self)
        self.mmts = mmts
        self.sshh = Sshh_helper(self)


    def clone_mmts_image(self, image=None, app=None):
        conn = app.img.conn_open_kvm2()
        x=0
        for xm in self.mmts.mmts_data:
            new_image = "mmts_node"+self.mmts.mmts_data[x].node_id+"--"+image[7:]
            self.mmts.mmts_data[x].images=new_image
            if app.img.check_for_availability(image=new_image, conn_open_kvm=conn) is None:
                app.img.clone_an_image(image=image, clone_name=new_image)

            st_image = app.img.start_image(name_image=new_image)
            self.mmts.mmts_data[x].images_ip=st_image.IP
            self.mmts.mmts_data[x].host = st_image.IP
            self.mmts.conn_mmts.conn_strings=self.mmts.conn_mmts.conn_strings+' dbname='+self.mmts.conn_mmts.dbname+\
                  " user="+self.mmts.conn_mmts.user+" host="+st_image.IP+" password="+self.mmts.conn_mmts.password+","




            x=x+1

        self.mmts.conn_mmts.conn_strings="'"+self.mmts.conn_mmts.conn_strings[:-1]+"'"
        print(self.mmts.mmts_data)
        print(self.mmts.conn_mmts)


    def tuning_mmts(self, ssh_trans=None):
        x = 0
        for xm in self.mmts.mmts_data:

            conn_ssh_str = Pgl_ssh(ip=xm.images_ip, username="test", password="TestPass1")

            # tuning pg_hba.conf
            ssh_command_str="sudo chmod 777 /var/lib/pgpro/ent-10/data/pg_hba.conf"
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str="sudo sed -i '$ a host     all        all        0.0.0.0\/0       md5' /var/lib/pgpro/ent-10/data/pg_hba.conf"
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str="sudo sed -i '$ a host     replication        repl        0.0.0.0\/0       trust' /var/lib/pgpro/ent-10/data/pg_hba.conf"
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            # tuning pg_hba.conf
            ssh_command_str = "sudo chmod 777 /var/lib/pgpro/ent-10/data/postgresql.conf"
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo sed -i "$ a wal_level = logical"  /var/lib/pgpro/ent-10/data/postgresql.conf'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo sed -i "$ a max_prepared_transactions = 600"  /var/lib/pgpro/ent-10/data/postgresql.conf'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo sed -i "$ a max_worker_processes = 500"  /var/lib/pgpro/ent-10/data/postgresql.conf'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo sed -i "$ a listen_addresses = \'*\' "  /var/lib/pgpro/ent-10/data/postgresql.conf'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo sed -i "$ a shared_preload_libraries = \'multimaster\' "  /var/lib/pgpro/ent-10/data/postgresql.conf'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = ('sudo sed -i "$ a multimaster.max_nodes = %s "  /var/lib/pgpro/ent-10/data/postgresql.conf' %
                               (self.mmts.conn_mmts.max_nodes))
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = ('sudo sed -i "$ a multimaster.node_id = %s "  /var/lib/pgpro/ent-10/data/postgresql.conf' %
                               (xm.node_id))
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = ('sudo sed -i "$ a multimaster.conn_strings = %s "  /var/lib/pgpro/ent-10/data/postgresql.conf' %
                               (self.mmts.conn_mmts.conn_strings))
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)



            ssh_command_str = 'sudo -H -u postgres psql -c "CREATE USER myuser WITH SUPERUSER ENCRYPTED PASSWORD \'myuserpassword\';"'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo -H -u postgres psql -c "CREATE DATABASE mydb OWNER myuser;"'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo pg-setup service stop'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

            ssh_command_str = 'sudo pg-setup service start'
            ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)

        time.sleep(20)
        conn_ssh_str = Pgl_ssh(ip=self.mmts.mmts_data[0].images_ip, username="test", password="TestPass1")
        ssh_command_str = 'sudo -H -u postgres psql -d mydb -c "CREATE EXTENSION multimaster;" '
        ssh_trans.ssh_trans_exec_command(conn_ssh_str=conn_ssh_str, ssh_command=ssh_command_str)











