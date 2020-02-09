#!/usr/bin/python3

# script to configure the WEB server
from pexpect import pxssh

# Login
# webIP=192.168.0.111
s = pxssh.pxssh()
s.login('192.168.0.111', 'egoad', 'RubberDuck!')
print("SSH login success")

# Run command
s.sendline('uptime')
s.prompt()
print(s.before)

# Logout
s.logout()
