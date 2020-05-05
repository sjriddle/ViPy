from scapy.all import *
from bluetooth import *

def retBtAddr(addr):
    bt_addr=str(hex(int(addr.replace(':', ''), 16) + 1))[2:]
    bt_addr=f'{bt_addr[0:2]}:{bt_addr[2:4]}:{bt_addr[4:6]}:{bt_addr[6:8]}:{bt_addr[8:10]}:{bt_addr[10:12]}'
    return btAddr


def checkBluetooth(bt_addr):
    bt_name = lookup_name(bt_addr)
    if bt_name:
        print(f'[+] Detected Bluetooth Device: {bt_name}')
    else:
        print('[-] Failed to Detect Bluetooth Device.')

        
def wifiPrint(pkt):
    iPhone_OUI = 'd0:23:db'
    if pkt.haslayer(Dot11):
        wifiMAC = pkt.getlayer(Dot11).addr2
        if iPhone_OUI == wifiMAC[:8]:
            print(f'[*] Detected iPhone MAC: {wifiMAC}')
            bt_addr = retBtAddr(wifiMAC)
            print(f'[+] Testing Bluetooth MAC: {bt_addr}')
            checkBluetooth(btAddr)

conf.iface = 'wlan0mon'
sniff(prn=wifiPrint)
