#!/usr/bin/python3
#Script to configure Web Server
import pexpect

#Connect and login
child = pexpect.spawn('ssh 192.168.0.111')
child.expect('.*password:')
child.sendline('Password01')
print("logged in success")

# Add a user
child.expect('\[.*~\]\$')
child.sendline('useradd egoad')
print(child.before)
child.expect('.*password:')
child.sendline('Password01')
print("user addded")
child.expect('\[.*~\]\$')
child.sendline('sudo passwd egoad')
child.expect('.*password:')
child.sendline('RubberDuck!')
child.expect('.*password:')
child.sendline('RubberDuck!')
child.expect(pexpect.EOF, timeout=None)

# Logout
child.expect('\[.*~\]\$')
print(child.before)
child.sendline('exit')
print("Logged out")

