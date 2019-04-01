import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Login Success.')
        ftp.quit()
        return True
    except:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Login Fail.')
        return False

host = '127.0.0.1'
anonLogin(host)
