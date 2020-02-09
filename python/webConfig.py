#!/usr/bin/python3
# Script to manage Web servers remotely
from pexpect import pxssh

# Login to Web1
s= pxssh.pxssh()
s.login('192.168.0.111', 'justincase', 'Password01')
print('SSH login success to Web1 server')

# Add User egoad
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print('Add user egoad success')

# Change User Password
s.prompt()
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print('Password change success for egoad user')

# Install Apache (httpd)
s.prompt()
s.sendline('sudo yum -y install httpd')
print('Apache install success')
s.prompt()
s.sendline('sudo systemctl start httpd')
print('Apache start success')
s.prompt()
s.sendline('sudo systemctl enable httpd')
print('Apache to start on boot success')

# Logout 
s.logout()
print('Web1 server Logged out')


# Login to Web2
s= pxssh.pxssh()
s.login('192.168.0.112', 'justincase', 'Password01')
print('SSH login success to Web2 server')

# Add User egoad
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print('Add user success')

# Change User Password
s.prompt()
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print('Password change success for egoad user')

# Install Apache (httpd)
s.prompt()
s.sendline('sudo yum -y install httpd')
print('Apache install success')
s.prompt()
s.sendline('sudo systemctl start httpd')
print('Apache start success')
s.prompt()
s.sendline('sudo systemctl enable httpd')
print('Apache to start on boot success')

# Logout
s.logout()
print('Web2 server Logged out')






