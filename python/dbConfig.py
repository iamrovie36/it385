#!/usr/bin/python3
# Script to manage DB servers remotely
from pexpect import pxssh

# Login to DB server
s= pxssh.pxssh()
s.login('192.168.0.121', 'justincase', 'Password01')
print('---SSH login success to DB1 server-')

# Add User egoad
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print('---Add user success-')

# Change User Password
s.prompt()
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')++++++++++++++++++++++6
s.prompt()
s.sendline('RubberDuck!')
print('---Password change success for egoad user-')

# Install MariaDB or MySQL
s.prompt()
s.sendline('sudo yum -y install mysql-server sql')
print('---MariaDB install success-')
s.prompt()
s.sendline('sudo systemctl start mariadb')
print('---MariaDB start success-')
s.prompt()
s.sendline('sudo systemctl enable mariadb')
print('---MariaDB to start on boot success-')

# Logout
s.logout()
print('----DB1 server Logged out-')


# Login to DB server
s= pxssh.pxssh()
s.login('192.168.0.122', 'justincase', 'Password01')
print('-----SSH login success to DB2 server-')

# Add User egoad
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print('-----Add user success-')

# Change User Password
s.prompt()
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')++++++++++++++++++++++6
s.prompt()
s.sendline('RubberDuck!')
print('-----Password change success for egoad user-')

# Install MariaDB or MySQL
s.prompt()
s.sendline('sudo yum -y install mysql-server mysql')
print('-----MariaDB install success-')
s.prompt()
s.sendline('sudo systemctl start mariadb')
print('-----MariaDB start success-')
s.prompt()
s.sendline('sudo systemctl enable mariadb')
print('-----MariaDB to start on boot success-')

# Logout
s.logout()
print('------DB2 server Logged out-')
