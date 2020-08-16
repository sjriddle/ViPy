import dpkt
import optparse
import socket

THRESH = 1000
def findDownload(pcap):
    for (ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        http = dpkt.http.Request(tcp.data)
        if http.method == 'GET':
            uri = http.uri.lower()
            print(f'[+] {socket.inet_ntoa(ip.src)} Download LOIC') if '.zip' in uri and 'loic' in uri else None

        
def findHivemind(pcap):
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        if tcp.dport == 6667:
            if '!lazor' in tcp.data.lower():
                print(f'[!] DDoS Hivemind issued by: {socket.inet_ntoa(ip.src)}')
                print(f'[+] Target CMD: {tcp.data}')
        if tcp.sport == 6667:
            if '!lazor' in tcp.data.lower():
                print(f'[!] DDoS Hivemind issued to: {socket.inet_ntoa(ip.src)}')
                print(f'[+] Target CMD: {tcp.data}')

        
def findAttack(pcap):
    pktCount = {}
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        if tcp.dport == 80:
            stream = f'{socket.inet_ntoa(ip.src)}:{socket.inet_ntoa(ip.dst)}'
            pktCount[stream] += 1 if pktCount.has_key(stream) else pktCount[stream] = 1

    for stream in pktCount:
        pktsSent = pktCount[stream]
        if pktsSent > THRESH:
            print(f"[+] {stream.split(':')[0]} attacked {stream.split(':')[1]} with {str(pktsSent)} pkts.")


def main():
    parser = optparse.OptionParser("usage %prog ' + '-p <pcap file> -t <thresh>")
    parser.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
    parser.add_option('-t', dest='thresh', type='int', help='specify threshold count ')

    options, args = parser.parse_args()
    if not options.pcapFile:
        print(parser.usage)
        exit(0)
    THRESH = options.thresh if options.thresh else THRESH
        
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)
    findDownload(pcap)
    findHivemind(pcap)
    findAttack(pcap)


if __name__ == '__main__':
    main()
