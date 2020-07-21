import dpkt
import socket

def printPcap(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = scoet.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'[+] src: {src} ---> dst: {dst}')
        except:
            raise Exception

def main():
    f = open('example.pcap')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)


if __name__ == '__main__':
    main()
