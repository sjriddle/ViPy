from bluetooth import *

def rfcomm_connection(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((adr,port))
        print(f'[+] RFCOMM Port {port} open')
        sock.close()
    except Exception, e:
        print(f'[+] RFCOMM Port {port} closed')

for port in range(1, 30):
    rfcomm_connection('{INSERT MAC ADDRESS}', port)
