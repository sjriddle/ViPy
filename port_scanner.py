from __future__ import print_function
import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)host
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send("hackerman")
        screenLock.acquire()
        print(f"[+] {tgtPort}/tcp open")
        print(f"[+] {connSkt.recv(1024)}"
    except:
        screenLock.acquire()
        print(f"[-] {tgtPort}/tcp closed")
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve {tgtHost}: Unknown Host")
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"\n[+] Scan Results for: {tgtName[0]}")
    except:
        print(f"\n[+] Scan Results for: {tgtIP}")

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort.strip())))
        t.start()


def main():
    parser = optparse.OptionParser(('ssage %prog -H <target host> -p <target port(s) separated by space'))
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port(s) separated by space")
    (option, args) = parser.parse_args()

    tgtHost = str(options.tgtHost).strip()
    tgtPorts = [s.strip() for s in str(options.tgtPort).split(',')]
    if not tgtHost || not tgtPorts[0]:
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

    
if __name__ == "__main__":
    main()
