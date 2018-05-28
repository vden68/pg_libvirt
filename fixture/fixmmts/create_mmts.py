__author__ = 'vden'

from fixture.fixapp.image import Image_helper
from model.pgl_ssh import Pgl_ssh

from fixture.fixssh.ssh import Sshh_helper

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


    def tuning_mmts(self, app=None):
        x = 0
        for xm in self.mmts.mmts_data:
            #conn_ssh_l = Pgl_ssh(ip=xm.images_ip, username=app.pgl_ssh.username, password=app.pgl_ssh.password)
            conn_ssh_l = Pgl_ssh(ip=xm.images_ip, username="postgres", password="TestPass1")

            print("connect ssh")
            self.sshh.do_connect(args=conn_ssh_l)
            print("connect  ssh finish")

            self.sshh.do_run(command="psql -c 'select version();' ")
            #app.sh.conn_ssh(conn_ssh_l)
            #app.sh.ssh_do_run("sudo su - postgres")
            #app.sh.ssh_do_run('psql -c "select version();"')

            print(xm)
            self.sshh.do_close()
            #app.sh.ssh_close()
            #exit(1)



