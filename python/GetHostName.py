#!/usr/bin/python3

# Sample script that gets hostnames
import pexpect

# Connect and login
child = pexpect.spawn('ssh 192.168.0.111')
child.expect('.*password:')
child.sendline('Password01')
print("logged in successfully")

# Run Hostname command
child.expect('\[.*~\]\$')
child.sendline('hostname')
print(child.before)
print("ran hostname command")

# logout
child.expect('\[.*~\]\$')
print(child.before)
child.sendline('exit')
print("Logged out")






