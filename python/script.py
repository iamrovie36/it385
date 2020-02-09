#!/usr/bin/python3

#Script to configure the server
from pexpect import pxssh
import pexpect

# login
s = pxssh.pxssh()
s.login('192.168.0.111', 'justincase', 'Password01')
print("SSH login success")

#Add user
s.sendline('uptime')
s.prompt()
print(s.before)
s.sendline('sudo useradd egoad')
s.prompt()
print(s.before)
s.sendline('sudo passwd egoad')
s.prompt()
print(s.before)




#Logout 
s.logout()
