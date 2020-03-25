import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print(f'\n[*] {str(hostname)} FTP Anonymous Login Success.')
        ftp.quit()
        return True
    except:
        print(f'\n[-] {(hostname)} FTP Anonymous Login Fail.')
        return False

host = '127.0.0.1'
anonLogin(host)
