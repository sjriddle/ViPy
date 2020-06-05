import threading
from scapy.all import *

def packet_callback(packet):
    if packet[TCP].payload:
        if ("user" or "pass") in  str(packet[TCP].payload).lower():
            print(f'[*] Server: {packet[IP].dst}')
            print(f'[*] {packet[TCP].payload}')

sniff(filter="TCP port 110 or TCP port 25 or TCP port 143", prn=packet_callback, store=0)
