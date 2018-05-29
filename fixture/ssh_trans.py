__author__ = 'vden'
import paramiko


class Ssh_trans:

    def __init__(self):
      pass




    def destroy(self):
        pass

    def ssh_trans_exec_command(self, conn_ssh_str=None, ssh_command=None):
        hostname, port, username, password = (conn_ssh_str.ip, 22, conn_ssh_str.username, conn_ssh_str.password)
        paramiko.util.log_to_file('trans.log')
        nbytes = 100
        trans = paramiko.Transport((hostname, int(port)))
        trans.connect(username=username, password=password)
        session = trans.open_channel('session')
        # Once the channel is established, we can execute only one command.Â  To execute another command, we need to create another channel
        session.exec_command(ssh_command)
        exit_status = session.recv_exit_status()
        stdout_data = []
        stderr_data = []

        while session.recv_ready():
            stdout_data.append(session.recv(nbytes).decode("utf-8", "ignore"))
            # stdout_data = b''.join(stdout_data)

        while session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes).decode("utf-8", "ignore"))
            # stderr_data = "".join(stderr_data)

        print("exit status ", exit_status)
        print("output")
        print(stdout_data)
        print("error")
        print(stderr_data)
        trans.close()