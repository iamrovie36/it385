#!/usr/bin/python3
# Script usin PXSSH to get uptime
from pexpect import pxssh

# Login
s = pxssh.pxssh()
s.login('192.168.0.111', 'justincase', 'Password01')
print("SSH login success")

# Run Command
s.sendline('uptime')
s.prompt()
print(s.before)

# Logout
s.logout()





