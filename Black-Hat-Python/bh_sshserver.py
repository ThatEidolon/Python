#!/usr/bin/python2.7

import socket
import subprocess
import paramiko
import sys

# using the key from the Paramiko demo file

host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server (paramike.ServerInterface):
    def _init_(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEED
        