#!/usr/bin/python
# -*- coding: utf-8 -*-
from bluetooth import *

def rfcommConnection(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((adr,port))
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception, e:
        print('[-] RFCOMM Port ' + str(port) + 'closed')

for port in range(1, 30):
    rfcommConnection('{INSERT MAC ADDRESS}', port)
