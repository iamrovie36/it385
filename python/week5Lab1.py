#!/usr/bin/python3

#Script to configure DB server using PXSSH
from pexpect import pxssh

# Login
s = pxssh.pxssh()
s.login('192.168.0.121', 'egoad', 'RubberDuck!')
print("SSH login success")


# Run command
s.sendline('uptime')
s.prompt()
print(s.before)

# Logout
s.logout()

