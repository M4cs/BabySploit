from configparser import ConfigParser
import platform, socket, os
config = ConfigParser()

def createuser():
    system = platform.system()
    release = platform.release()
    config['DEFAULT'] = {
        'lhost': '0.0.0.0',
        'lport': '8080',
        'rhost': 'google.com',
        'rport': '80',
        'platform': '',
        'usernamelist': 'lists/users',
        'passwordlist': 'lists/pass/rockyou.txt',
        'urlpath': '/connect'
    }
    config['DEFAULT']['platform'] = "%s %s" % (system, release)
    with open("babysploit/config/config.cfg", "w") as configfile:
        config.write(configfile)

def checkuser():
    if os.path.exists("babysploit/config/config.cfg") == True:
        print("          [i] Loaded Configuration... [i]")
    else:
        createuser()
        print("     [i] Created New Configuration File... [i]")

